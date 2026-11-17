import base64
import json
import unittest
import uuid
from datetime import datetime, timezone

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

from frontier_identity import Verifier

ISSUER = "demo-issuer-01"
KID = "demo-key-01"
NOW = datetime(2030, 1, 1, 12, 0, tzinfo=timezone.utc)


def make_payload(**changes):
    payload = {
        "schema_version": "0.1",
        "credential_id": str(uuid.uuid4()),
        "issuer_id": ISSUER,
        "issued_at": "2030-01-01T11:00:00Z",
        "expires_at": "2030-01-02T11:00:00Z",
        "subject_ref": str(uuid.uuid4()),
        "credential_type": "TRAINING_CREDENTIAL",
    }
    payload.update(changes)
    return payload


def sign(payload, private_key):
    protected = {"alg": "Ed25519", "kid": KID}
    encoded = json.dumps(
        {"protected": protected, "payload": payload},
        sort_keys=True, separators=(",", ":"), ensure_ascii=False,
        allow_nan=False
    ).encode("utf-8")
    return {
        "protected": protected,
        "payload": payload,
        "signature": base64.b64encode(private_key.sign(encoded)).decode("ascii"),
    }


class VerifierTests(unittest.TestCase):
    def setUp(self):
        self.private_key = Ed25519PrivateKey.generate()
        self.events = []
        self.verifier = Verifier(
            {ISSUER: {KID: self.private_key.public_key()}},
            clock=lambda: NOW,
            audit_sink=self.events.append,
        )

    def test_valid_synthetic_credential(self):
        result = self.verifier.verify(sign(make_payload(), self.private_key))
        self.assertEqual(result.status, "VALID_FOR_DEMO")
        self.assertEqual(result.reason, "all_configured_demo_checks_passed")

    def test_malformed_payload_rejected(self):
        payload = make_payload()
        del payload["subject_ref"]
        result = self.verifier.verify(sign(payload, self.private_key))
        self.assertEqual(result.status, "INVALID_FORMAT")

    def test_unknown_issuer_rejected(self):
        payload = make_payload(issuer_id="unconfigured-demo-issuer")
        result = self.verifier.verify(sign(payload, self.private_key))
        self.assertEqual(result.status, "UNKNOWN_ISSUER")

    def test_tampered_payload_fails_signature(self):
        envelope = sign(make_payload(), self.private_key)
        envelope["payload"]["credential_type"] = "ALTERED"
        result = self.verifier.verify(envelope)
        self.assertEqual(result.status, "INVALID_FORMAT")
        # Unsupported claim type is rejected before signature verification.
        envelope = sign(make_payload(), self.private_key)
        envelope["payload"]["subject_ref"] = str(uuid.uuid4())
        envelope["payload"]["credential_id"] = str(uuid.uuid4())
        envelope["payload"]["issued_at"] = "2030-01-01T11:00:00Z"
        envelope["payload"]["expires_at"] = "2030-01-02T11:00:00Z"
        envelope["payload"]["schema_version"] = "0.1"
        envelope["payload"]["issuer_id"] = ISSUER
        envelope["payload"]["credential_type"] = "TRAINING_CREDENTIAL"
        envelope["payload"]["tampered"] = "yes"
        result = self.verifier.verify(envelope)
        self.assertEqual(result.status, "INVALID_FORMAT")

    def test_signature_failure_for_modified_signed_claim(self):
        envelope = sign(make_payload(), self.private_key)
        envelope["payload"]["subject_ref"] = str(uuid.uuid4())
        result = self.verifier.verify(envelope)
        self.assertEqual(result.status, "INTEGRITY_FAILED")

    def test_expired_credential(self):
        payload = make_payload(
            issued_at="2029-12-30T11:00:00Z",
            expires_at="2029-12-31T11:00:00Z",
        )
        result = self.verifier.verify(sign(payload, self.private_key))
        self.assertEqual(result.status, "EXPIRED")

    def test_duplicate_presentation(self):
        envelope = sign(make_payload(), self.private_key)
        self.assertEqual(self.verifier.verify(envelope).status, "VALID_FOR_DEMO")
        self.assertEqual(
            self.verifier.verify(envelope).status, "DUPLICATE_PRESENTATION"
        )

    def test_audit_event_does_not_contain_payload(self):
        payload = make_payload()
        result = self.verifier.verify(sign(payload, self.private_key))
        event = self.events[-1]
        self.assertEqual(result.correlation_id, event["correlation_id"])
        self.assertEqual(event["event_type"], "credential_verification")
        self.assertNotIn(payload["subject_ref"], str(event))
        self.assertNotIn(payload["credential_id"], str(event))
        self.assertEqual(
            set(event),
            {"timestamp", "correlation_id", "event_type", "result", "reason", "schema_version"},
        )

    def test_naive_clock_fails_closed(self):
        verifier = Verifier(
            {ISSUER: {KID: self.private_key.public_key()}},
            clock=lambda: datetime(2030, 1, 1, 12, 0),
        )
        result = verifier.verify(sign(make_payload(), self.private_key))
        self.assertEqual(result.status, "REVIEW_REQUIRED")

    def test_signed_header_cannot_be_substituted(self):
        verifier = Verifier(
            {ISSUER: {KID: self.private_key.public_key(),
                      "alternate-kid": self.private_key.public_key()}},
            clock=lambda: NOW,
        )
        envelope = sign(make_payload(), self.private_key)
        envelope["protected"]["kid"] = "alternate-kid"
        result = verifier.verify(envelope)
        self.assertEqual(result.status, "INTEGRITY_FAILED")

    def test_non_utc_timestamp_rejected(self):
        payload = make_payload(issued_at="2030-01-01T11:00:00+01:00")
        result = self.verifier.verify(sign(payload, self.private_key))
        self.assertEqual(result.status, "INVALID_FORMAT")

    def test_future_credential_requires_review(self):
        payload = make_payload(
            issued_at="2030-01-01T13:00:00Z",
            expires_at="2030-01-02T13:00:00Z",
        )
        result = self.verifier.verify(sign(payload, self.private_key))
        self.assertEqual(result.status, "REVIEW_REQUIRED")


if __name__ == "__main__":
    unittest.main()
