"""Local-only verifier for fictional, synthetic credentials.

This module validates a demo credential. It does not identify a human subject.
"""

from __future__ import annotations

import base64
import binascii
import json
import re
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Callable, Mapping

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

SCHEMA_VERSION = "0.1"
ALGORITHM = "Ed25519"
CREDENTIAL_TYPE = "TRAINING_CREDENTIAL"
MAX_PAYLOAD_BYTES = 4096
PAYLOAD_FIELDS = {
    "schema_version",
    "credential_id",
    "issuer_id",
    "issued_at",
    "expires_at",
    "subject_ref",
    "credential_type",
}
ENVELOPE_FIELDS = {"protected", "payload", "signature"}
PROTECTED_FIELDS = {"alg", "kid"}
UTC_TIMESTAMP = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?Z$"
)


@dataclass(frozen=True)
class VerificationResult:
    status: str
    reason: str
    correlation_id: str


class Verifier:
    """Verify signatures and claims against explicitly configured demo keys."""

    def __init__(
        self,
        trusted_issuers: Mapping[str, Mapping[str, Ed25519PublicKey]],
        clock: Callable[[], datetime] | None = None,
        audit_sink: Callable[[dict[str, str]], None] | None = None,
    ) -> None:
        self._trusted_issuers = {
            issuer: dict(keys) for issuer, keys in trusted_issuers.items()
        }
        self._clock = clock or (lambda: datetime.now(timezone.utc))
        self._audit_sink = audit_sink or (lambda _event: None)
        self._seen_credential_ids: set[str] = set()

    def verify(self, envelope: object) -> VerificationResult:
        correlation_id = str(uuid.uuid4())
        status, reason = self._verify(envelope)
        event = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "correlation_id": correlation_id,
            "event_type": "credential_verification",
            "result": status,
            "reason": reason,
            "schema_version": SCHEMA_VERSION,
        }
        # The event is allow-listed: no payload, subject reference, key or signature.
        self._audit_sink(event)
        return VerificationResult(status, reason, correlation_id)

    def _verify(self, envelope: object) -> tuple[str, str]:
        if type(envelope) is not dict or set(envelope) != ENVELOPE_FIELDS:
            return "INVALID_FORMAT", "envelope_shape_invalid"

        protected = envelope["protected"]
        payload = envelope["payload"]
        signature_text = envelope["signature"]
        if type(protected) is not dict or set(protected) != PROTECTED_FIELDS:
            return "INVALID_FORMAT", "protected_header_invalid"
        if protected.get("alg") != ALGORITHM:
            return "INVALID_FORMAT", "unsupported_algorithm"
        if type(protected.get("kid")) is not str or not protected["kid"]:
            return "INVALID_FORMAT", "key_id_invalid"
        if type(payload) is not dict or set(payload) != PAYLOAD_FIELDS:
            return "INVALID_FORMAT", "payload_shape_invalid"
        if type(signature_text) is not str or len(signature_text) != 88:
            return "INVALID_FORMAT", "signature_encoding_invalid"

        if any(type(value) is not str for value in payload.values()):
            return "INVALID_FORMAT", "payload_value_type_invalid"
        if payload["schema_version"] != SCHEMA_VERSION:
            return "INVALID_FORMAT", "schema_version_unsupported"
        if payload["credential_type"] != CREDENTIAL_TYPE:
            return "INVALID_FORMAT", "credential_type_unsupported"
        if not self._is_uuid(payload["credential_id"]):
            return "INVALID_FORMAT", "credential_id_invalid"
        if not self._is_uuid(payload["subject_ref"]):
            return "INVALID_FORMAT", "subject_ref_invalid"
        if not payload["issuer_id"] or len(payload["issuer_id"]) > 64:
            return "INVALID_FORMAT", "issuer_id_invalid"

        try:
            issued_at = self._parse_utc(payload["issued_at"])
            expires_at = self._parse_utc(payload["expires_at"])
        except ValueError:
            return "INVALID_FORMAT", "timestamp_invalid"
        if expires_at <= issued_at:
            return "INVALID_FORMAT", "validity_interval_invalid"

        try:
            signed_bytes = json.dumps(
                {"protected": protected, "payload": payload},
                sort_keys=True,
                separators=(",", ":"),
                ensure_ascii=False,
                allow_nan=False,
            ).encode("utf-8")
        except (TypeError, ValueError, UnicodeEncodeError):
            return "INVALID_FORMAT", "payload_serialization_invalid"
        if len(signed_bytes) > MAX_PAYLOAD_BYTES:
            return "INVALID_FORMAT", "payload_too_large"

        issuer_keys = self._trusted_issuers.get(payload["issuer_id"])
        if issuer_keys is None:
            return "UNKNOWN_ISSUER", "issuer_not_configured"
        public_key = issuer_keys.get(protected["kid"])
        if public_key is None:
            return "UNKNOWN_ISSUER", "key_id_not_configured"

        try:
            signature = base64.b64decode(signature_text, validate=True)
            public_key.verify(signature, signed_bytes)
        except (binascii.Error, ValueError, InvalidSignature):
            return "INTEGRITY_FAILED", "signature_verification_failed"

        now = self._clock()
        if now.tzinfo is None or now.utcoffset() is None:
            return "REVIEW_REQUIRED", "verifier_clock_not_timezone_aware"
        now = now.astimezone(timezone.utc)
        if now < issued_at:
            return "REVIEW_REQUIRED", "credential_not_yet_valid"
        if now >= expires_at:
            return "EXPIRED", "credential_expired"

        credential_id = payload["credential_id"]
        if credential_id in self._seen_credential_ids:
            return "DUPLICATE_PRESENTATION", "credential_already_seen"
        self._seen_credential_ids.add(credential_id)
        return "VALID_FOR_DEMO", "all_configured_demo_checks_passed"

    @staticmethod
    def _is_uuid(value: str) -> bool:
        try:
            return str(uuid.UUID(value)) == value
        except (ValueError, AttributeError):
            return False

    @staticmethod
    def _parse_utc(value: str) -> datetime:
        if not UTC_TIMESTAMP.fullmatch(value):
            raise ValueError("timestamp must be UTC RFC 3339 with Z suffix")
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
        if parsed.tzinfo is None or parsed.utcoffset() is None:
            raise ValueError("timestamp must be timezone-aware")
        return parsed.astimezone(timezone.utc)
