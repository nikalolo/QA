# Behaviour-level traceability

Generated from the CSV definitions and behaviour map. Links show design coverage, not confirmed requirements or successful execution.

26/26 proposed requirements and 43/43 listed behaviours have mapped cases. This is not exhaustive application coverage.

Cases: 45; design-blocked: 10. Latest case statuses: BLOCKED=0, FAIL=2, NOT EXECUTED=27, PASS=16.

| Behaviour | Requirement | Proposed behaviour | Cases | Latest execution status | Bug IDs |
|---|---|---|---|---|---|
| B-01 | REQ-NAV-01 | Home content | TC-001 | TC-001: PASS | None recorded |
| B-02 | REQ-NAV-01 | Header/footer destinations | TC-002 | TC-002: NOT EXECUTED | None recorded |
| B-03 | REQ-NAV-02 | Back and forward navigation | TC-003 | TC-003: NOT EXECUTED | None recorded |
| B-04 | REQ-SRCH-01 | Matching keyword | TC-004 | TC-004: PASS | None recorded |
| B-05 | REQ-SRCH-01 | Empty search policy | TC-006 | TC-006: NOT EXECUTED | None recorded |
| B-06 | REQ-SRCH-01 | HTML-like and punctuation inputs | TC-007; TC-045 | TC-007: NOT EXECUTED; TC-045: NOT EXECUTED | None recorded |
| B-07 | REQ-SRCH-02 | No matches | TC-005 | TC-005: PASS | None recorded |
| B-08 | REQ-FILT-01 | Price ascending sort | TC-008 | TC-008: PASS | None recorded |
| B-09 | REQ-FILT-01 | Category filtering | TC-009 | TC-009: PASS | None recorded |
| B-10 | REQ-FILT-01 | Brand filtering | TC-041 | TC-041: NOT EXECUTED | None recorded |
| B-11 | REQ-PROD-01 | Name, price, description, add control | TC-010 | TC-010: PASS | None recorded |
| B-12 | REQ-CART-01 | Add and indicator | TC-011 | TC-011: PASS | None recorded |
| B-13 | REQ-CART-02 | Quantity, line and cart totals | TC-012 | TC-012: FAIL | BUG-001 |
| B-14 | REQ-CART-03 | Zero policy | TC-013 | TC-013: NOT EXECUTED | None recorded |
| B-15 | REQ-CART-03 | Negative quantity | TC-035 | TC-035: NOT EXECUTED | None recorded |
| B-16 | REQ-CART-03 | Fractional quantity | TC-036 | TC-036: NOT EXECUTED | None recorded |
| B-17 | REQ-CART-03 | Extreme quantity policy | TC-014 | TC-014: NOT EXECUTED | None recorded |
| B-18 | REQ-CART-04 | Removal and empty state | TC-015 | TC-015: NOT EXECUTED | None recorded |
| B-19 | REQ-REG-01 | Valid registration | TC-016 | TC-016: PASS | None recorded |
| B-20 | REQ-REG-02 | Required fields | TC-017 | TC-017: PASS | None recorded |
| B-21 | REQ-REG-02 | Correction and retained data | TC-030 | TC-030: NOT EXECUTED | None recorded |
| B-22 | REQ-REG-03 | Email partitions | TC-018; TC-037 | TC-018: NOT EXECUTED; TC-037: NOT EXECUTED | None recorded |
| B-23 | REQ-REG-03 | Password rules | TC-019 | TC-019: FAIL | BUG-002 |
| B-24 | REQ-REG-04 | Duplicate email | TC-020 | TC-020: NOT EXECUTED | None recorded |
| B-25 | REQ-REG-05 | Future DOB | TC-021 | TC-021: NOT EXECUTED | None recorded |
| B-26 | REQ-REG-05 | Very old DOB | TC-038 | TC-038: NOT EXECUTED | None recorded |
| B-27 | REQ-LOGIN-01 | Valid login | TC-022 | TC-022: PASS | None recorded |
| B-28 | REQ-LOGIN-02 | Wrong password | TC-023 | TC-023: PASS | None recorded |
| B-29 | REQ-LOGIN-02 | Required fields | TC-024 | TC-024: PASS | None recorded |
| B-30 | REQ-LOGIN-03 | Logout and protected access | TC-025 | TC-025: PASS | None recorded |
| B-31 | REQ-CHK-01 | Checkout entry | TC-026 | TC-026: NOT EXECUTED | None recorded |
| B-32 | REQ-CHK-02 | Required address fields | TC-027 | TC-027: NOT EXECUTED | None recorded |
| B-33 | REQ-CHK-02 | Postcode rule | TC-039 | TC-039: NOT EXECUTED | None recorded |
| B-34 | REQ-CHK-03 | Valid path to payment stage | TC-042 | TC-042: NOT EXECUTED | None recorded |
| B-35 | REQ-CONT-01 | Valid submission | TC-028 | TC-028: PASS | None recorded |
| B-36 | REQ-CONT-02 | Required fields | TC-029 | TC-029: PASS | None recorded |
| B-37 | REQ-CONT-02 | Email format | TC-040 | TC-040: PASS | None recorded |
| B-38 | REQ-UI-01 | Visual consistency | TC-031 | TC-031: NOT EXECUTED | None recorded |
| B-39 | REQ-RESP-01 | 375 px layout/navigation | TC-032 | TC-032: NOT EXECUTED | None recorded |
| B-40 | REQ-RESP-01 | 768 px layout/navigation | TC-033 | TC-033: NOT EXECUTED | None recorded |
| B-41 | REQ-COMP-01 | Login in both browsers | TC-034 | TC-034: NOT EXECUTED | None recorded |
| B-42 | REQ-COMP-01 | Cart in both browsers | TC-043 | TC-043: NOT EXECUTED | None recorded |
| B-43 | REQ-COMP-01 | Checkout in both browsers | TC-044 | TC-044: NOT EXECUTED | None recorded |

Run-level history: [execution log](../test-cases/execution-log.csv). Details: [test cases](../test-cases/test-cases.md). Defects: [verified findings](../bug-reports/verified-findings.md).
