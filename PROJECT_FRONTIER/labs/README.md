# Project Frontier Laboratories

All labs are educational, defensive, and isolated.

## Permitted environments

- Local toy applications and intentionally vulnerable training targets.
- Synthetic identity records and fictional workflows.
- Public aggregate datasets.
- Systems for which explicit written authorisation covers the exact test.

## Prohibited without explicit authorisation

- Scanning, probing, or testing government, immigration, border, police, airport, or third-party systems.
- Accessing real traveller, passport, biometric, personnel, or operational records.
- Bypassing access controls or attempting to obtain credentials.
- Sending test traffic to live production systems outside a written scope.

## Lab record template

Each lab should record:
1. Objective and learning outcome.
2. Environment and versions.
3. Scope and authorisation status.
4. Synthetic inputs or sample provenance.
5. Steps performed.
6. Expected and actual observations.
7. Evidence files and hashes where appropriate.
8. Findings and limitations.
9. Defensive recommendations.
10. Cleanup and reproducibility instructions.

## Current lab tracks

- [Digital Identity Laboratory](digital-identity/README.md) — design stage; synthetic credentials only. No verifier implementation is claimed.
- Networking fundamentals and packet interpretation — planned isolated baseline lab.

## Lab sequencing

The networking baseline validates core infrastructure concepts. The digital identity lab is being specified in parallel, but implementation remains gated on review of its data contract and threat model.

Do not begin with live-target scanning. First establish the ability to explain IP addressing, DNS, TCP handshakes, HTTP requests, TLS at a conceptual level, and the limits of packet captures.
