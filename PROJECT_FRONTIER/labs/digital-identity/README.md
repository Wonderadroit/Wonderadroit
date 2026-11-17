# Digital Identity Laboratory

## Purpose

Build a small, local educational demonstration of an identity-credential verification workflow. The lab explores data minimisation, input validation, issuer authenticity, credential integrity, expiry handling, access control, and privacy-aware audit records.

This is **not** a passport-verification product, biometric system, border-control tool, or production identity service.

## Safety boundary

- Use fictional names and generated identifiers only.
- Do not use real passport numbers, national identity numbers, dates of birth, photographs, biometrics, traveller records, or government datasets.
- Do not connect to NIS, immigration, police, airport, border, national identity, or other operational systems.
- Do not make eligibility, admissibility, fraud, risk, or enforcement decisions.
- No face recognition, biometric matching, document OCR, or real credential scanning in this first version.
- The demonstration must return evidence states, not a person's risk score.

## Narrow use case

A fictional training operator submits a synthetic digital credential. The verifier checks:
1. required fields and strict formats;
2. whether the credential was issued by a locally configured demonstration issuer;
3. whether the signed payload is intact;
4. whether the credential is within its validity period;
5. whether the credential identifier has already been seen in the demonstration store.

The output is a transparent review state:
- `VALID_FOR_DEMO`
- `INVALID_FORMAT`
- `UNKNOWN_ISSUER`
- `INTEGRITY_FAILED`
- `EXPIRED`
- `DUPLICATE_PRESENTATION`
- `REVIEW_REQUIRED`

These labels describe only the synthetic lab checks. They do not establish a real person's identity or legal status.

## Design constraints

- Local-only execution; no network listener or external API.
- Synthetic fixtures checked into the repository.
- Explicit versioned schema.
- Cryptographic signing must use a vetted standard library and documented algorithm; never invent a signature scheme or roll custom cryptography.
- Private signing material must be generated at runtime and excluded from Git.
- Audit events must contain event type, timestamp, opaque lab correlation ID, and result code only; never log the credential payload or personal fields.
- Deterministic tests must use a fixed test clock and isolated temporary storage.
- A duplicate is a repeat of the same synthetic credential identifier in this lab, not a claim of fraud.

## Planned implementation sequence

1. Approve the data contract and threat model.
2. Implement schema validation and deterministic test fixtures.
3. Add issuer signature verification using a standard cryptographic library.
4. Add validity and duplicate checks with a test clock.
5. Add privacy-minimised audit events.
6. Add tests, setup instructions, limitations, and a reproducibility record.

## Acceptance criteria

- Every result is tied to a named check and machine-readable reason.
- Invalid, expired, unknown-issuer, tampered, and duplicate fixtures are covered by tests.
- No test requires real personal data or external connectivity.
- Audit output contains no credential payload or direct identity fields.
- The README and threat model clearly state that successful verification proves only integrity/issuer/validity checks within this toy system—not that the subject is the person presenting it.
- All tests pass in a documented environment.

## Implementation status

A first local verifier implementation and unit-test suite now exist. It uses Ed25519 through the maintained `cryptography` library, a fixed demo issuer/key configuration, strict schema checks, UTC validity checks, in-memory duplicate detection, and allow-listed audit events.

This is an initial implementation, not yet a validated release. CI execution, test review, and the documented limitations remain outstanding. No real identity capability is claimed.
