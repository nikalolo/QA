# Test design and data

Positive tests cover valid registration, login, cart and checkout. Negative tests isolate an invalid input while all other fields are valid. TC-017/TC-027/TC-029 deliberately retain one empty-form submission as a validation checklist; record each field outcome. The checkout journey TC-042 stays together because reaching payment with intact order data is its single purpose.

## Partitions and boundaries

- Quantity: positive whole numbers (proposed valid partition), zero policy unknown, negative integers, fractions, extremes. TC-035 and TC-036 isolate two invalid partitions.
- Email: missing domain (`abc@`, TC-018) and missing at sign (`abc.com`, TC-037). These examples do not exhaust email syntax.
- DOB: future and extremely old values are separate tests (TC-021, TC-038).
- `999999` and `1900-01-01` are robustness/extreme inputs, not verified boundaries.

If the confirmed integer range is MIN–MAX, design separate data iterations for MIN−1, MIN, MIN+1, MAX−1, MAX, MAX+1. Record one result per iteration; deduplicate overlapping points in narrow ranges.

| Domain | MIN | MAX | Unit / rule | Candidate values | Expected results | Readiness |
|---|---|---|---|---|---|---|
| Quantity | TBD | TBD | Whole units; stock policy TBD | TBD for all six points | TBD | BLOCKED — REQUIREMENT UNCLEAR (Q-02) |
| DOB / age | TBD | TBD | Calendar dates or age; timezone TBD | TBD around confirmed cutoffs | TBD | BLOCKED — REQUIREMENT UNCLEAR (Q-04) |
| Password length | TBD | TBD | Length and composition TBD | TBD around confirmed limits | TBD | BLOCKED — REQUIREMENT UNCLEAR (Q-03) |

These are design templates, not additional counted tests or completed BVA. After clarification, add concrete cases with new IDs and update the behaviour map.

## Data and isolation

Record exact product ID/name/URL/price, category/brand, search term and dataset/build in `Data used` or the execution log. Angle-bracket placeholders are values to collect, never current product claims. Use synthetic accounts and addresses; record account aliases, not passwords/tokens. Use a unique email allowed by the demo's confirmed rules. Do not assume demo credentials exist.

Before each negative registration/contact/address test, establish an otherwise valid dataset. Reset cart, session and filters between independent cases. Record shared-demo resets or unavailable setup as BLOCKED during an attempted run. Keep valid quantity 3 conditional on confirmed availability.

High = core purchase/account access or high-impact validation; Medium = secondary behaviour; Low = visual polish or speculative DOB checks. Adjust priorities if observed risk changes.
