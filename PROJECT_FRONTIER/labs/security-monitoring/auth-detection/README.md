# Authentication Detection Laboratory

## Objective

Demonstrate a small, reproducible, defensive detection workflow using synthetic authentication events. The lab ingests JSON Lines (JSONL), validates records, removes duplicate event IDs, orders events by timestamp, correlates failures by source IP and username, and emits a structured alert.

This is an educational batch detector. It is **not** a production SIEM, an authentication control, or proof that an account was compromised.

## Safety and scope

- All records are fictional and use documentation-only IP ranges.
- Do not add real usernames, credentials, personal data, traveller records, or government operational logs.
- Do not connect this lab to production systems.
- No network scanning or live authentication attempts are required.

## Detection rule: FRONTIER-AUTH-001

Generate a HIGH-severity alert (FRONTIER-AUTH-001) when at least five failed authentication events are followed by a successful authentication for the **same username and source IP** within a rolling ten-minute window.

Generate a MEDIUM-severity alert (FRONTIER-AUTH-002) when at least five failed authentication events occur for the **same username and source IP** within a rolling ten-minute window, even if no successful login follows. The alert is emitted once per burst; a successful login or expiry of the rolling failure window resets the burst state. If a later successful login follows the failures, FRONTIER-AUTH-001 may also fire as a separate, stronger correlation signal.

The correlation key includes both username and source IP to avoid combining failures against different accounts that happen to originate from one shared address.

A generated alert is an investigative lead, not a finding of malicious activity. Legitimate causes may include user error, stale service credentials, shared egress addresses, or authorised testing.

## Requirements

- Python 3.10 or later
- Python standard library only

## Run

From this directory:

```bash
python detector.py
```

Use another JSONL file:

```bash
python detector.py path/to/events.jsonl
```

Run the regression tests:

```bash
python -m unittest -v
```

## Input contract

Each non-empty line must be a JSON object containing:

- `event_id`: unique event identifier
- `timestamp`: ISO 8601 timestamp with timezone
- `source_ip`: valid IPv4 or IPv6 address
- `username`: non-empty account identifier
- `event_type`: `authentication_failure` or `authentication_success`

Malformed records and duplicate event IDs are skipped and reported. Events are sorted by timestamp before correlation. The first occurrence of a duplicate event ID is retained.

## Tests

The regression suite covers:

- Positive detection for failure-then-success correlation.
- Brute-force detection at the threshold without requiring a successful login.
- Brute-force negative case below threshold, per-burst alert suppression, key isolation, window expiry/re-arming, and success reset.
- Below-threshold negative case.
- Success outside the time window.
- Different usernames and source IPs.
- Out-of-order input.
- Exact window boundary.
- Clearing the failure sequence after a successful login.
- Duplicate event IDs.
- Malformed JSON and invalid IP addresses.

## Known limitations

- Batch processing only; no streaming, state persistence, alert deduplication across runs, or distributed correlation.
- Assumes event timestamps are trustworthy and clocks are sufficiently synchronised.
- No enrichment, asset criticality, allow-listing, user identity resolution, or baseline modelling.
- Thresholds are fixed defaults and require environment-specific tuning before operational use.
- The brute-force rule is a simple event-count heuristic; legitimate retries, shared NAT, automated clients and password-manager errors can produce false positives.
- Does not inspect packet payloads or establish data exfiltration.
- Does not establish whether an authentication success was authorised or malicious.

## Evidence and completion gate

A positive fixture alone is insufficient. The lab is considered regression-tested only when the full automated suite passes in the local environment and the GitHub Actions run. Record the commit, workflow run, test output, and limitations before making a validation claim.
