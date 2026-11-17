# Synthetic Credential Data Contract

**Version:** 0.1-draft  
**Status:** Proposed contract; implementation must not begin until reviewed.

## Purpose

Define the smallest fictional credential needed to test format validation, issuer trust, integrity, expiry, and duplicate presentation.

## Envelope

A submitted credential consists of two parts:

- `protected`: fixed algorithm identifier, key identifier, and schema version.
- `payload`: synthetic credential claims.
- `signature`: signature bytes encoded using the selected standard encoding.

The exact serialization and signature format will be fixed during implementation. The verifier must reject unsupported algorithms rather than accept an algorithm chosen by untrusted input.

## Payload fields

| Field | Type | Rule | Reason |
|---|---|---|---|
| `schema_version` | string | Exact supported version | Prevent ambiguous parsing |
| `credential_id` | string | Random synthetic UUID | Duplicate-presentation demonstration |
| `issuer_id` | string | Must match configured demo issuer | Issuer allow-list |
| `issued_at` | string | UTC RFC 3339 timestamp | Temporal validation |
| `expires_at` | string | UTC RFC 3339 timestamp, later than issue time | Expiry validation |
| `subject_ref` | string | Random synthetic reference; no name or date of birth | Demonstrate a subject reference without direct identifiers |
| `credential_type` | string | Fixed allow-listed demo type | Type validation |

## Deliberately excluded

- Full name, address, phone, email, date of birth.
- Passport, national identity, or immigration document numbers.
- Photograph, face template, fingerprint, iris, voice, or other biometric.
- Nationality, ethnicity, religion, political information, or travel history.
- Operational status, watchlist status, risk score, or eligibility conclusion.

## Validation rules

- Reject unknown fields unless a later schema version explicitly defines them.
- Reject missing required fields, wrong JSON types, invalid UUIDs, malformed timestamps, and unsupported schema versions.
- Parse timestamps as timezone-aware UTC values; reject naive timestamps.
- Require `expires_at > issued_at`.
- Enforce a documented maximum payload size.
- Never echo submitted values in errors or logs.
- Verify the signature over one precisely defined canonical representation. Do not implement signing until canonicalisation and algorithm choices are documented.

## Result semantics

A successful result means only that the synthetic payload passed the configured lab's schema, issuer, signature, validity, and duplicate checks. It does **not** authenticate the human presenter, prove a legal identity, validate a real document, or establish immigration eligibility.

## Open design decision

Choose and document a well-supported standard signature format and maintained Python library before implementation. Pin the algorithm in verifier code; do not let the credential select arbitrary algorithms.
