# Threat Model — Synthetic Digital Identity Lab

**Status:** Initial design; to be reviewed before implementation.  
**System:** Local-only educational verifier using fictional credentials.  
**Security objective:** Demonstrate transparent verification checks while minimising data collection and preventing misleading claims.

## Assets

- Synthetic credential payloads.
- Demonstration issuer public key and ephemeral private signing key.
- Local duplicate-detection store.
- Verification result and minimal audit event.
- Test fixtures and test clock.

No real identity data, operational keys, government records, or production secrets are in scope.

## Trust boundaries

1. **Input boundary:** all submitted JSON is untrusted, including values from checked-in fixtures.
2. **Issuer boundary:** only a locally configured demonstration issuer is trusted by this lab.
3. **Verifier boundary:** validation and cryptographic verification occur locally.
4. **Persistence boundary:** duplicate state and audit events are stored locally in a disposable lab directory.
5. **Repository boundary:** private keys, local databases, generated credentials, and runtime logs must not be committed.

## Threats and controls

| Threat | Example | Planned control | Residual limitation |
|---|---|---|---|
| Malformed input | Missing or wrong-type fields | Strict schema and type validation | Schema validity does not prove identity |
| Payload tampering | A field changes after signing | Verify signature over canonical payload bytes | Signing does not prove the presenter is the subject |
| Unknown issuer | Credential claims an unconfigured issuer | Explicit issuer allow-list | Local allow-list is not a real trust framework |
| Expired credential | Validity end precedes fixed test time | UTC-aware validity checks and test clock | Clock correctness is assumed in the toy lab |
| Replay / duplicate | Same synthetic credential ID presented twice | Local duplicate store and explicit duplicate result | Not distributed replay prevention; store can be reset |
| Sensitive logging | Full credential copied into logs | Allow-listed audit fields only | Host-level logging and filesystem access remain outside scope |
| Key disclosure | Private test key committed | Runtime key generation, ignore rules, key-path checks | Local device compromise is not solved |
| Algorithm confusion | Input selects a weak or unsupported algorithm | Pin one documented algorithm in code/config | No algorithm agility or production key lifecycle |
| False assurance | A valid signature is mistaken for proof of personhood | Explicit result semantics and limitations | Human readers may still overinterpret results |

## Abuse cases explicitly out of scope

- Real passport or national-ID validation.
- Biometric capture, matching, or liveness detection.
- Traveller profiling, watchlist matching, risk scoring, or automated adverse decisions.
- Connection to government or third-party identity services.
- Production deployment, high availability, distributed revocation, or legal identity proofing.

## Privacy and data minimisation

The verifier should process only the fields required by the synthetic schema. Audit events should record:
- UTC timestamp;
- random lab correlation ID;
- check/result code;
- software/schema version.

Audit events must not include names, dates of birth, credential contents, signatures, or stable personal identifiers.

## Review questions before implementation

- Is the schema minimal enough for the learning objective?
- Is the signing format canonical and unambiguous?
- Are errors specific enough for reproducibility without exposing payload values?
- Can a reader distinguish issuer authenticity, payload integrity, credential validity, and subject authentication?
- Are generated secrets and runtime data excluded from version control?
