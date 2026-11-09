# Requirements analysis

Requirements remain proposed/ASSUMED unless a source is cited. Real application observations and executions are recorded in the feature inventory and case history. Observations do not establish intended behaviour. UI title v5.0; footer v2.5 Built 2026-10-11 observed.

Use `CONFIRMED — SPECIFICATION` only with an authoritative source, version and relevant clause. Use `OBSERVED — TO BE VERIFIED` for application behaviour with environment, date and evidence. Observation alone does not establish intended behaviour. Resolve conflicts as questions, not automatic expected-result changes.

| ID | Proposed requirement | Status | Source / evidence |
| --- | --- | --- | --- |
| REQ-NAV-01 | Main navigation links lead to the correct pages without errors | ASSUMED | TBD |
| REQ-NAV-02 | Back restores the list; Forward restores the selected product identity and URL. | ASSUMED | TBD |
| REQ-SRCH-01 | Search follows a confirmed matching and empty/special-input policy (Q-01). | ASSUMED | TBD |
| REQ-SRCH-02 | A search with no matches shows a clear no-results message | ASSUMED | TBD |
| REQ-FILT-01 | Users can filter by category/brand and sort products | ASSUMED | TBD |
| REQ-PROD-01 | A product page shows name, price, description and an add-to-cart control | ASSUMED | TBD |
| REQ-CART-01 | Adding a product updates the cart indicator | ASSUMED | TBD |
| REQ-CART-02 | Quantity can be changed and line/cart totals update | ASSUMED | TBD |
| REQ-CART-03 | Quantity is a positive whole number; zero, limits and invalid-input handling need clarification (Q-02). | ASSUMED | TBD |
| REQ-CART-04 | A product can be removed from the cart | ASSUMED | TBD |
| REQ-REG-01 | A new user can register with valid data | ASSUMED | TBD |
| REQ-REG-02 | Required registration fields show validation; correction retains non-secret data and permits valid submission. | ASSUMED | TBD |
| REQ-REG-03 | Invalid email formats and passwords violating confirmed rules are rejected (Q-03). | ASSUMED | TBD |
| REQ-REG-04 | A duplicate email cannot be registered | ASSUMED | TBD |
| REQ-REG-05 | DOB follows a confirmed date/age range policy (Q-04). | ASSUMED | TBD |
| REQ-LOGIN-01 | A registered user can log in with valid credentials | ASSUMED | TBD |
| REQ-LOGIN-02 | Invalid credentials are rejected with a clear, non-revealing error | ASSUMED | TBD |
| REQ-LOGIN-03 | Logout ends the session; protected pages are no longer accessible | ASSUMED | TBD |
| REQ-CHK-01 | Checkout can be started from the cart | ASSUMED | TBD |
| REQ-CHK-02 | Required address fields prevent progression when empty; postcode policy needs clarification (Q-05). | ASSUMED | TBD |
| REQ-CONT-01 | The contact form can be submitted with valid data | ASSUMED | TBD |
| REQ-CONT-02 | Contact form validates mandatory fields and email format | ASSUMED | TBD |
| REQ-UI-01 | Fonts, buttons and spacing are consistent across pages | ASSUMED | TBD |
| REQ-RESP-01 | Layout is usable at 375 px and 768 px widths without horizontal scrolling | ASSUMED | TBD |
| REQ-COMP-01 | Login, cart addition and checkout to payment stage satisfy the same functional criteria in recorded Chrome and Firefox versions. | ASSUMED | TBD |
| REQ-CHK-03 | A valid user can proceed from product selection through checkout to the payment stage, without submitting payment. | ASSUMED | TBD |

See [behaviour traceability](04-traceability.md), [open questions](open-questions.md) and [design techniques](05-test-design.md). A mapped case demonstrates design coverage, not validated requirements or successful testing.

Before execution, confirm each assertion, mandatory-field list and runtime dataset. Additional observed features belong in the inventory first; do not silently broaden scope. Combined filters, other sort modes, session expiry and persistence remain exploration candidates, not claimed detailed coverage.
