# HYPOTHETICAL learning example — NOT a real finding

Example ID: EXAMPLE-01 (not part of verified defect counts).
Scenario: cart line total remains unchanged after quantity increases from 1 to 3.

- Illustrative setup: fictional product priced at 10.00 units, quantity 1, no other lines or adjustments. These are teaching values, not Toolshop product data.
- Environment/build/date: not executed; a real report must record exact values.
- Steps: open cart; set quantity to 3; commit; read line total.
- Hypothetical expected result: 30.00, if confirmed pricing rule is unit price × quantity.
- Hypothetical actual result: 10.00. This symptom was not observed.
- Suggested severity: High if incorrect amount affects checkout; Medium may fit a display-only issue when checkout is correct. Verify impact first.
- Suggested priority: High if reproducible in a core purchase flow; actual urgency needs triage context.
- Reproducibility/status: NOT EXECUTED / HYPOTHETICAL.
- Evidence to collect if encountered: before/after totals, exact item/price, relevant redacted request/response. No attachments exist.

Weak report: “Cart is broken sometimes.” It omits data, steps, expected/actual results and environment.
