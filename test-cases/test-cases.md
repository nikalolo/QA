# Manual test cases

Generated from `test-cases.csv`; edit that file, not this view. See [execution instructions](README.md).

Expected results are proposed oracles until reviewed. Design blockers are separate from execution status.

Total: 45 cases

## TC-001 — Home page displays navigation and catalogue

| Field | Value |
|---|---|
| Requirement | REQ-NAV-01 |
| Behaviour IDs | B-01 |
| Priority | High |
| Design status | READY — requirement reviewed |
| Open question |  |
| Preconditions | Confirmed app URL; clean browser session |
| Test data | &lt;app URL and build recorded&gt; |
| Steps | 1. Open app URL. 2. Wait for loading to finish. 3. Inspect header, catalogue and footer. |
| Expected result | Home content, navigation and product list are visible; no error page replaces them. |
| Actual result | Home, navigation, catalogue and footer visible; no error page. |
| Status | PASS |
| Data used | Combination Pliers 01M6C0W2EQJKMKPC1P43PQ4P93; $14.15; empty login credentials for TC-024 |
| Environment / date | 2026-11-01 Asia/Tbilisi; Windows host; ChatGPT in-app browser, version/viewport not recorded; UI v2.5 build 2026-10-11 |
| Notes / evidence | evidence/screenshots/test-execution/home-2026-11-01.png |
| Bug ID |  |

## TC-002 — Main navigation destinations

| Field | Value |
|---|---|
| Requirement | REQ-NAV-01 |
| Behaviour IDs | B-02 |
| Priority | High |
| Design status | ASSUMED — confirm requirement before execution |
| Open question |  |
| Preconditions | Navigation inventory with expected destinations approved |
| Test data | &lt;header and footer link-to-destination list&gt; |
| Steps | 1. Open home. 2. Follow each inventoried link. 3. Record destination and result per link. 4. Return home before the next link. |
| Expected result | Every destination matches the recorded target; no error page. Any failing link fails this navigation checklist. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-003 — Back and forward restore list and selected product

| Field | Value |
|---|---|
| Requirement | REQ-NAV-02 |
| Behaviour IDs | B-03 |
| Priority | Medium |
| Design status | ASSUMED — confirm requirement before execution |
| Open question |  |
| Preconditions | Unfiltered product list open |
| Test data | &lt;existing product selected during execution&gt;; record ID, name, URL, unit price and currency |
| Steps | 1. Record list URL. 2. Open selected product and record URL. 3. Press Back. 4. Press Forward. |
| Expected result | Back returns to the list URL and list content; Forward returns to the same product URL and identity. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-004 — Search a known matching keyword

| Field | Value |
|---|---|
| Requirement | REQ-SRCH-01 |
| Behaviour IDs | B-04 |
| Priority | High |
| Design status | READY — requirement reviewed |
| Open question |  |
| Preconditions | No selected filters; exact known product name from live catalogue. Broader Q-01 matching rules remain open. |
| Test data | &lt;keyword from verified product&gt;; &lt;expected matching product IDs&gt; |
| Steps | 1. Clear filters. 2. Enter keyword and submit. 3. Inspect all result pages against the recorded matching rule. |
| Expected result | For exact known product name Combination Pliers, return the known matching product and no nonmatching names (explicit scoped portfolio assumption). |
| Actual result | Search Combination Pliers returned one product: Combination Pliers $14.15; no pagination or nonmatching products. |
| Status | PASS |
| Data used | Exact name Combination Pliers; returned ID 01M6C4A0S1M9BATY0NANAQEB7Y |
| Environment / date | 2026-11-01 Asia/Tbilisi; Windows host; in-app browser version/viewport unavailable; v2.5 build 2026-10-11 |
| Notes / evidence | evidence/screenshots/test-execution/search-known-product.png |
| Bug ID |  |

## TC-005 — Search a known no-match term

| Field | Value |
|---|---|
| Requirement | REQ-SRCH-02 |
| Behaviour IDs | B-07 |
| Priority | Medium |
| Design status | READY — requirement reviewed |
| Open question |  |
| Preconditions | Dataset checked for absence of term |
| Test data | zzzzqqq; replace and record if it exists in the dataset |
| Steps | 1. Clear filters. 2. Search the recorded no-match term. |
| Expected result | Zero product cards are shown and a visible no-results message explains the empty state. |
| Actual result | Search zzzzqqq completed: 0 products found and There are no products found; no product cards. |
| Status | PASS |
| Data used | Combination Pliers $14.15; quantity 3; search zzzzqqq; public demo customer alias Jane Doe (secrets omitted) |
| Environment / date | 2026-11-01 Asia/Tbilisi; Windows host; in-app browser version/viewport unrecorded; UI v2.5 build 2026-10-11 |
| Notes / evidence | evidence/screenshots/test-execution/search-no-results.png |
| Bug ID |  |

## TC-006 — Empty search policy

| Field | Value |
|---|---|
| Requirement | REQ-SRCH-01 |
| Behaviour IDs | B-05 |
| Priority | Low |
| Design status | BLOCKED — REQUIREMENT UNCLEAR |
| Open question | Q-01 |
| Preconditions | Q-01 resolved; record one approved outcome |
| Test data | Empty string |
| Steps | 1. Clear search and filters. 2. Submit an empty search. |
| Expected result | TBD: specify exact result set and message from Q-01 before execution. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-007 — HTML-like search input is displayed as text

| Field | Value |
|---|---|
| Requirement | REQ-SRCH-01 |
| Behaviour IDs | B-06 |
| Priority | Medium |
| Design status | BLOCKED — REQUIREMENT UNCLEAR |
| Open question | Q-01 |
| Preconditions | Q-01 resolved; exact search response approved |
| Test data | &lt;b&gt;test&lt;/b&gt; |
| Steps | 1. Enter the literal input. 2. Submit. 3. Inspect any reflected text and result state. |
| Expected result | TBD: record search outcome from Q-01; any reflected input must remain literal text, with no injected bold element. This is input handling, not a penetration test. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-008 — Sort prices in ascending order

| Field | Value |
|---|---|
| Requirement | REQ-FILT-01 |
| Behaviour IDs | B-08 |
| Priority | Medium |
| Design status | READY — requirement reviewed |
| Open question |  |
| Preconditions | Unfiltered product list with at least two different prices |
| Test data | Price ascending option; record prices and currency |
| Steps | 1. Select ascending price sort. 2. Record displayed prices across result pages. |
| Expected result | Each successive price is greater than or equal to the preceding price, including page transitions. |
| Actual result | Price Low-High verified across all five pages: page boundaries 9.17 to 10.07, 13.41 to 13.96, 20.14 to 20.33, 45.23 to 46.50; last price 89.55. Every displayed price nondecreasing. |
| Status | PASS |
| Data used | Live catalogue 45 products, ascending price sort, pages 1–5; USD display. |
| Environment / date | 2026-11-01 Asia/Tbilisi; Windows host; in-app browser exact version/viewport unrecorded; UI v2.5 build 2026-10-11 |
| Notes / evidence | evidence/screenshots/test-execution/price-sort-pages.txt |
| Bug ID |  |

## TC-009 — Filter by one category

| Field | Value |
|---|---|
| Requirement | REQ-FILT-01 |
| Behaviour IDs | B-09 |
| Priority | Medium |
| Design status | READY — requirement reviewed |
| Open question |  |
| Preconditions | Category membership of sample products recorded |
| Test data | &lt;existing category&gt;; record label and known member IDs |
| Steps | 1. Clear filters. 2. Select category. 3. Inspect results across pages. |
| Expected result | Known category members are present; every returned product belongs to the chosen category. |
| Actual result | Hand Saw selected with no other filters: one returned product Wood Saw $12.18, ID 01M6C4A0VTBB4RTKNKFFCWPTNA; opened details and confirmed category Hand Saw. No pagination. |
| Status | PASS |
| Data used | Wood Saw; ID 01M6C4A0VTBB4RTKNKFFCWPTNA; $12.18; Hand Saw category; quantity 1. |
| Environment / date | 2026-11-01 Asia/Tbilisi; Windows host; in-app browser version/viewport not recorded; UI v2.5 build 2026-10-11 |
| Notes / evidence | Execution recorded in execution-log.csv; no dedicated screenshot required. |
| Bug ID |  |

## TC-010 — Product detail content

| Field | Value |
|---|---|
| Requirement | REQ-PROD-01 |
| Behaviour IDs | B-11 |
| Priority | High |
| Design status | READY — requirement reviewed |
| Open question |  |
| Preconditions | Product list open |
| Test data | &lt;existing product selected during execution&gt;; record ID, name, URL, unit price and currency |
| Steps | 1. Record selected card name and price. 2. Open details. 3. Inspect name, price, description and add control. |
| Expected result | Name and price match selected card; description is nonempty and add-to-cart control is visible. |
| Actual result | Combination Pliers card and detail both $14.15; description nonempty; Add to cart visible. |
| Status | PASS |
| Data used | Combination Pliers 01M6C0W2EQJKMKPC1P43PQ4P93; $14.15; empty login credentials for TC-024 |
| Environment / date | 2026-11-01 Asia/Tbilisi; Windows host; ChatGPT in-app browser, version/viewport not recorded; UI v2.5 build 2026-10-11 |
| Notes / evidence | evidence/screenshots/test-execution/product-2026-11-01.png |
| Bug ID |  |

## TC-011 — Add one product updates cart

| Field | Value |
|---|---|
| Requirement | REQ-CART-01 |
| Behaviour IDs | B-12 |
| Priority | High |
| Design status | READY — requirement reviewed |
| Open question |  |
| Preconditions | Empty cart; product available |
| Test data | &lt;existing product selected during execution&gt;; record ID, name, URL, unit price and currency; quantity 1 |
| Steps | 1. Open details. 2. Add quantity 1. 3. Open cart. |
| Expected result | Indicator shows 1; cart contains the selected product once with quantity 1. |
| Actual result | Empty fresh session: added Wood Saw quantity 1. Cart badge DOM span cart-quantity showed 1; cart contained Wood Saw once, quantity 1, unit/line $12.18. Displayed eco discount $0.61 and grand total $11.57. |
| Status | PASS |
| Data used | Wood Saw; ID 01M6C4A0VTBB4RTKNKFFCWPTNA; $12.18; Hand Saw category; quantity 1. |
| Environment / date | 2026-11-01 Asia/Tbilisi; Windows host; in-app browser version/viewport not recorded; UI v2.5 build 2026-10-11 |
| Notes / evidence | evidence/screenshots/test-execution/final-cart.txt |
| Bug ID |  |

## TC-012 — Change quantity recalculates totals

| Field | Value |
|---|---|
| Requirement | REQ-CART-02 |
| Behaviour IDs | B-13 |
| Priority | High |
| Design status | READY — requirement reviewed |
| Open question |  |
| Preconditions | One product at quantity 1; quantity 3 permitted; price and pricing rules recorded |
| Test data | &lt;existing product selected during execution&gt;; record ID, name, URL, unit price and currency; quantity 3 |
| Steps | 1. Open cart. 2. Set quantity to 3 and commit. 3. Independently calculate line total and cart total. |
| Expected result | Line total equals unit price × 3; cart total equals sum of lines plus/minus only confirmed displayed adjustments. |
| Actual result | Quantity 1 to 3 changed line total from $14.15 to $42.45 but grand total remained $14.15. Refresh restored quantity 1. Repeated with Tab and Enter. |
| Status | FAIL |
| Data used | Combination Pliers $14.15; quantity 3; search zzzzqqq; public demo customer alias Jane Doe (secrets omitted) |
| Environment / date | 2026-11-01 Asia/Tbilisi; Windows host; in-app browser version/viewport unrecorded; UI v2.5 build 2026-10-11 |
| Notes / evidence | evidence/screenshots/bugs/BUG-001-grand-total.png; evidence/screenshots/devtools/BUG-001-console.json |
| Bug ID | BUG-001 |

## TC-013 — Zero quantity policy

| Field | Value |
|---|---|
| Requirement | REQ-CART-03 |
| Behaviour IDs | B-14 |
| Priority | High |
| Design status | BLOCKED — REQUIREMENT UNCLEAR |
| Open question | Q-02 |
| Preconditions | One item at quantity 1; Q-02 resolved |
| Test data | 0 |
| Steps | 1. Enter 0 in quantity. 2. Commit. 3. Inspect quantity, message and totals. |
| Expected result | TBD: confirm whether zero is rejected or removes the item, then record one expected cart state and total. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-014 — Extreme quantity input

| Field | Value |
|---|---|
| Requirement | REQ-CART-03 |
| Behaviour IDs | B-17 |
| Priority | Medium |
| Design status | BLOCKED — REQUIREMENT UNCLEAR |
| Open question | Q-02 |
| Preconditions | One item at quantity 1; Q-02 resolved |
| Test data | 999999 (robustness value, not a known boundary) |
| Steps | 1. Enter 999999. 2. Commit. 3. Inspect quantity, message and totals. |
| Expected result | TBD: record accepted/rejected outcome and exact resulting quantity/total from Q-02. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-015 — Remove the only cart item

| Field | Value |
|---|---|
| Requirement | REQ-CART-04 |
| Behaviour IDs | B-18 |
| Priority | High |
| Design status | ASSUMED — confirm requirement before execution |
| Open question |  |
| Preconditions | One item in cart |
| Test data | &lt;existing product selected during execution&gt;; record ID, name, URL, unit price and currency |
| Steps | 1. Remove the item. 2. Inspect cart and indicator. |
| Expected result | Removed item is absent, empty-cart message is visible, indicator represents zero items and no positive merchandise total remains. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-016 — Register a valid new account

| Field | Value |
|---|---|
| Requirement | REQ-REG-01 |
| Behaviour IDs | B-19 |
| Priority | High |
| Design status | READY — requirement reviewed |
| Open question |  |
| Preconditions | Fresh logged-out session; approved fake registration dataset recorded; all fields except the target are valid; unique email |
| Test data | Nika Test; &lt;unique test email&gt;; &lt;password meeting confirmed rules, kept private&gt;; remaining valid fake fields recorded before execution |
| Steps | 1. Open registration. 2. Fill recorded valid dataset. 3. Submit once. 4. Record confirmation and resulting account state. |
| Expected result | Registration succeeds with confirmation; the new account identity matches submitted data. Login is checked separately in TC-022. |
| Actual result | Synthetic registration submitted; redirected to login; subsequent login displayed Portfolio Tester at /account. |
| Status | PASS |
| Data used | Portfolio Tester; DOB 1995-01-01; Austria; postcode 1010; house 98; phone synthetic 123456789; portfolio-qa-1101-unique@example.com. Address autofill replaced entered street/city/state with Marvin-Krenn-Gasse/Mittersill/Vorarlberg. Password values omitted. |
| Environment / date | 2026-11-01 Asia/Tbilisi; Windows host; in-app browser exact version/viewport unavailable; v2.5 build 2026-10-11 |
| Notes / evidence | evidence/screenshots/test-execution/registered-account.png |
| Bug ID |  |

## TC-017 — Registration required-field validation

| Field | Value |
|---|---|
| Requirement | REQ-REG-02 |
| Behaviour IDs | B-20 |
| Priority | High |
| Design status | READY — requirement reviewed |
| Open question |  |
| Preconditions | Required-field list confirmed; fresh form |
| Test data | All required fields empty |
| Steps | 1. Open registration. 2. Submit empty form. 3. Record validation per required field. |
| Expected result | Each required field is identified by a readable validation message; registration is prevented. |
| Actual result | Empty registration submission displayed required messages for first/last name, DOB, country, postcode, house number, street, city, state, phone, email and password; registration prevented. |
| Status | PASS |
| Data used | Contact: Portfolio Tester; portfolio-test@example.com (abc for negative case); Customer service; message: Disposable QA portfolio practice message for contact form validation only. No reply required. Registration: all fields blank. |
| Environment / date | 2026-11-01 Asia/Tbilisi; Windows host; in-app browser version/viewport unrecorded; UI v2.5 build 2026-10-11 |
| Notes / evidence | evidence/screenshots/test-execution/registration-required.png |
| Bug ID |  |

## TC-018 — Registration email lacks domain

| Field | Value |
|---|---|
| Requirement | REQ-REG-03 |
| Behaviour IDs | B-22 |
| Priority | High |
| Design status | ASSUMED — confirm requirement before execution |
| Open question |  |
| Preconditions | Fresh logged-out session; approved fake registration dataset recorded; all fields except the target are valid; unique email |
| Test data | Email abc@; all other fields valid |
| Steps | 1. Fill valid dataset with email abc@. 2. Submit. |
| Expected result | Email validation explains invalid format; registration is prevented. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-019 — Registration password violates confirmed rule

| Field | Value |
|---|---|
| Requirement | REQ-REG-03 |
| Behaviour IDs | B-23 |
| Priority | High |
| Design status | READY — requirement reviewed |
| Open question |  |
| Preconditions | Fresh logged-out session; approved fake registration dataset recorded; all fields except the target are valid; unique email |
| Test data | &lt;password violating exactly one confirmed rule; keep value private&gt; |
| Steps | 1. Record the violated rule and use otherwise valid data. 2. Submit. |
| Expected result | Password violating visible 8-character help rule is rejected with validation accurately identifying the violated length rule; messages must be consistent. |
| Actual result | Six-character mixed password rejected, but error claims minimal 6 while help says at least 8. Other fields populated; longer password allowed registration. |
| Status | FAIL |
| Data used | Portfolio Tester; DOB 1995-01-01; Austria; postcode 1010; house 98; phone synthetic 123456789; portfolio-qa-1101-unique@example.com. Address autofill replaced entered street/city/state with Marvin-Krenn-Gasse/Mittersill/Vorarlberg. Password values omitted. |
| Environment / date | 2026-11-01 Asia/Tbilisi; Windows host; in-app browser exact version/viewport unavailable; v2.5 build 2026-10-11 |
| Notes / evidence | evidence/screenshots/bugs/BUG-002-password-guidance.png |
| Bug ID | BUG-002 |

## TC-020 — Duplicate email registration

| Field | Value |
|---|---|
| Requirement | REQ-REG-04 |
| Behaviour IDs | B-24 |
| Priority | High |
| Design status | ASSUMED — confirm requirement before execution |
| Open question |  |
| Preconditions | Fresh logged-out session; approved fake registration dataset recorded; all fields except the target are valid; unique email; existing test account email known |
| Test data | &lt;existing test account email&gt;; other fields valid |
| Steps | 1. Fill registration using existing email. 2. Submit. |
| Expected result | Duplicate registration is prevented with a visible explanation; no second account is created. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-021 — Future date of birth policy

| Field | Value |
|---|---|
| Requirement | REQ-REG-05 |
| Behaviour IDs | B-25 |
| Priority | Low |
| Design status | BLOCKED — REQUIREMENT UNCLEAR |
| Open question | Q-04 |
| Preconditions | Fresh logged-out session; approved fake registration dataset recorded; all fields except the target are valid; unique email |
| Test data | Execution date + 1 calendar day; record exact date and timezone |
| Steps | 1. Enter future DOB with other fields valid. 2. Submit. |
| Expected result | TBD: record future-date acceptance policy and expected message from Q-04. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-022 — Valid account login

| Field | Value |
|---|---|
| Requirement | REQ-LOGIN-01 |
| Behaviour IDs | B-27 |
| Priority | High |
| Design status | READY — requirement reviewed |
| Open question |  |
| Preconditions | Logged out; known valid test account available |
| Test data | &lt;test account email&gt;; password kept private |
| Steps | 1. Open login. 2. Enter valid credentials. 3. Submit. |
| Expected result | Authenticated account page is accessible and displays the expected test account identity. |
| Actual result | Documented demo customer login succeeded; /account displayed My account and Jane Doe. |
| Status | PASS |
| Data used | Combination Pliers $14.15; quantity 3; search zzzzqqq; public demo customer alias Jane Doe (secrets omitted) |
| Environment / date | 2026-11-01 Asia/Tbilisi; Windows host; in-app browser version/viewport unrecorded; UI v2.5 build 2026-10-11 |
| Notes / evidence | evidence/screenshots/test-execution/login-account.png |
| Bug ID |  |

## TC-023 — Wrong password rejected

| Field | Value |
|---|---|
| Requirement | REQ-LOGIN-02 |
| Behaviour IDs | B-28 |
| Priority | High |
| Design status | READY — requirement reviewed |
| Open question |  |
| Preconditions | Logged out; valid test account available |
| Test data | Existing email; deliberately wrong password kept private |
| Steps | 1. Enter email and wrong password. 2. Submit. 3. Try recorded protected account URL. |
| Expected result | Login fails with non-revealing credentials error; protected account content is inaccessible. |
| Actual result | Wrong password for documented demo customer displayed Invalid email or password. Direct /account/profile request redirected to /auth/login; no protected profile values visible. |
| Status | PASS |
| Data used | Documented demo customer Jane Doe; protected URL https://practicesoftwaretesting.com/account/profile; credentials omitted. |
| Environment / date | 2026-11-01 Asia/Tbilisi; Windows host; in-app browser exact version/viewport unavailable; UI v2.5 build 2026-10-11 |
| Notes / evidence | evidence/screenshots/test-execution/logout-protected-login.png |
| Bug ID |  |

## TC-024 — Empty login validation

| Field | Value |
|---|---|
| Requirement | REQ-LOGIN-02 |
| Behaviour IDs | B-29 |
| Priority | Medium |
| Design status | READY — requirement reviewed |
| Open question |  |
| Preconditions | Logged out; empty login form |
| Test data | Empty email and password |
| Steps | 1. Submit empty form. |
| Expected result | Both required fields have readable validation; no authenticated session is created. |
| Actual result | Submitted empty checkout login form: Email is required and Password is required displayed; remained unauthenticated. |
| Status | PASS |
| Data used | Combination Pliers 01M6C0W2EQJKMKPC1P43PQ4P93; $14.15; empty login credentials for TC-024 |
| Environment / date | 2026-11-01 Asia/Tbilisi; Windows host; ChatGPT in-app browser, version/viewport not recorded; UI v2.5 build 2026-10-11 |
| Notes / evidence | Execution recorded in execution-log.csv; no dedicated screenshot required. |
| Bug ID |  |

## TC-025 — Logout prevents protected access

| Field | Value |
|---|---|
| Requirement | REQ-LOGIN-03 |
| Behaviour IDs | B-30 |
| Priority | High |
| Design status | READY — requirement reviewed |
| Open question |  |
| Preconditions | Logged in; protected URL recorded |
| Test data | &lt;protected account URL&gt; |
| Steps | 1. Log out. 2. Press Back. 3. Reload. 4. Directly open protected URL. |
| Expected result | Logout removes authenticated access; refreshed and directly requested protected content requires login. |
| Actual result | Logged in as Jane Doe and loaded populated /account/profile. Signed out; used Back and reload; directly reopened /account/profile. Final route /auth/login, no authenticated profile values exposed. |
| Status | PASS |
| Data used | Documented demo customer Jane Doe; protected URL https://practicesoftwaretesting.com/account/profile; credentials omitted. |
| Environment / date | 2026-11-01 Asia/Tbilisi; Windows host; in-app browser exact version/viewport unavailable; UI v2.5 build 2026-10-11 |
| Notes / evidence | evidence/screenshots/test-execution/logout-protected-login.png |
| Bug ID |  |

## TC-026 — Start checkout from cart

| Field | Value |
|---|---|
| Requirement | REQ-CHK-01 |
| Behaviour IDs | B-31 |
| Priority | High |
| Design status | ASSUMED — confirm requirement before execution |
| Open question |  |
| Preconditions | Logged in; one available item in cart |
| Test data | &lt;existing product selected during execution&gt;; record ID, name, URL, unit price and currency |
| Steps | 1. Open cart. 2. Activate checkout. |
| Expected result | Checkout opens with the same selected item and quantity available in its order summary. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-027 — Empty checkout address validation

| Field | Value |
|---|---|
| Requirement | REQ-CHK-02 |
| Behaviour IDs | B-32 |
| Priority | High |
| Design status | ASSUMED — confirm requirement before execution |
| Open question |  |
| Preconditions | At address step; required fields confirmed |
| Test data | All required address fields empty |
| Steps | 1. Clear required address fields. 2. Attempt to continue. |
| Expected result | Each missing required field is identified; progression to payment is prevented. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-028 — Valid contact submission

| Field | Value |
|---|---|
| Requirement | REQ-CONT-01 |
| Behaviour IDs | B-35 |
| Priority | Medium |
| Design status | READY — requirement reviewed |
| Open question |  |
| Preconditions | Valid subject/options and message limits confirmed |
| Test data | Nika Test; &lt;test email&gt;; &lt;valid subject&gt;; message: QA practice contact message; adjust to confirmed limits |
| Steps | 1. Open contact form. 2. Enter valid recorded data. 3. Submit once. |
| Expected result | Visible success confirmation is shown. Delivery to an external inbox is not asserted. |
| Actual result | Submitted Portfolio Tester / portfolio-test@example.com / Customer service / 91-character synthetic message; confirmation: Thanks for your message! We will contact you shortly. No inbox delivery asserted. |
| Status | PASS |
| Data used | Contact: Portfolio Tester; portfolio-test@example.com (abc for negative case); Customer service; message: Disposable QA portfolio practice message for contact form validation only. No reply required. Registration: all fields blank. |
| Environment / date | 2026-11-01 Asia/Tbilisi; Windows host; in-app browser version/viewport unrecorded; UI v2.5 build 2026-10-11 |
| Notes / evidence | evidence/screenshots/test-execution/contact-success.png |
| Bug ID |  |

## TC-029 — Empty contact form validation

| Field | Value |
|---|---|
| Requirement | REQ-CONT-02 |
| Behaviour IDs | B-36 |
| Priority | Medium |
| Design status | READY — requirement reviewed |
| Open question |  |
| Preconditions | Contact required fields confirmed; empty form |
| Test data | All required fields empty |
| Steps | 1. Submit empty contact form. 2. Record each validation. |
| Expected result | Required fields are identified by readable messages; success confirmation is absent and submission is prevented. |
| Actual result | Empty contact submission displayed First name is required, Last name is required, Email is required, Subject is required and Message is required; no success confirmation. |
| Status | PASS |
| Data used | Contact: Portfolio Tester; portfolio-test@example.com (abc for negative case); Customer service; message: Disposable QA portfolio practice message for contact form validation only. No reply required. Registration: all fields blank. |
| Environment / date | 2026-11-01 Asia/Tbilisi; Windows host; in-app browser version/viewport unrecorded; UI v2.5 build 2026-10-11 |
| Notes / evidence | Execution recorded in execution-log.csv; no dedicated screenshot required. |
| Bug ID |  |

## TC-030 — Correct registration validation error

| Field | Value |
|---|---|
| Requirement | REQ-REG-02 |
| Behaviour IDs | B-21 |
| Priority | Medium |
| Design status | ASSUMED — confirm requirement before execution |
| Open question |  |
| Preconditions | Fresh logged-out session; approved fake registration dataset recorded; all fields except the target are valid; unique email |
| Test data | Valid dataset except blank first name; then Nika |
| Steps | 1. Submit with only first name blank. 2. Record other non-secret values. 3. Fill first name. 4. Re-enter secret fields if required by confirmed policy. 5. Submit. |
| Expected result | First-name error clears; non-secret values are retained; corrected registration succeeds. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-031 — Visual consistency across pages

| Field | Value |
|---|---|
| Requirement | REQ-UI-01 |
| Behaviour IDs | B-38 |
| Priority | Low |
| Design status | ASSUMED — confirm requirement before execution |
| Open question |  |
| Preconditions | Same browser, viewport and zoom; approved visual comparison baseline |
| Test data | Home, product, cart, registration, login, checkout, contact |
| Steps | 1. Open each listed page. 2. Compare repeated controls with baseline. 3. Record per-page differences. |
| Expected result | No overlapping controls or clipped essential text; labels align with their fields; equivalent control roles use matching font, colour and spacing from the approved baseline; intentional exceptions are recorded. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-032 — Responsive layout and navigation at 375 px

| Field | Value |
|---|---|
| Requirement | REQ-RESP-01 |
| Behaviour IDs | B-39 |
| Priority | High |
| Design status | ASSUMED — confirm requirement before execution |
| Open question |  |
| Preconditions | Browser emulation; zoom 100%; valid test data prepared |
| Test data | 375x667 CSS px; Home, product, cart, registration, login, checkout, contact |
| Steps | 1. Set viewport. 2. Visit each listed page. 3. Open menu and navigate. 4. Focus fields and trigger validation. 5. Record each page result. |
| Expected result | No unintended horizontal page scroll, overlapping controls or clipped essential text; labels and fields remain aligned; text can be read at 100% zoom; primary controls can be activated and focused; navigation reaches intended pages. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-033 — Responsive layout and navigation at 768 px

| Field | Value |
|---|---|
| Requirement | REQ-RESP-01 |
| Behaviour IDs | B-40 |
| Priority | Medium |
| Design status | ASSUMED — confirm requirement before execution |
| Open question |  |
| Preconditions | Browser emulation; zoom 100%; valid test data prepared |
| Test data | 768x1024 CSS px; Home, product, cart, registration, login, checkout, contact |
| Steps | 1. Set viewport. 2. Visit each listed page. 3. Open menu and navigate. 4. Focus fields and trigger validation. 5. Record each page result. |
| Expected result | No unintended horizontal page scroll, overlapping controls or clipped essential text; labels and fields remain aligned; text can be read at 100% zoom; primary controls can be activated and focused; navigation reaches intended pages. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-034 — Login compatibility in Chrome and Firefox

| Field | Value |
|---|---|
| Requirement | REQ-COMP-01 |
| Behaviour IDs | B-41 |
| Priority | High |
| Design status | ASSUMED — confirm requirement before execution |
| Open question |  |
| Preconditions | Both browsers installed; versions recorded; clean logged-out sessions |
| Test data | Same test account; 1366x768; 100% zoom |
| Steps | 1. Execute TC-022 in Chrome. 2. Execute TC-022 independently in Firefox. 3. Record separate execution rows. |
| Expected result | Both browsers independently satisfy TC-022 expected result. A shared failure is still a failure. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-035 — Negative quantity rejected

| Field | Value |
|---|---|
| Requirement | REQ-CART-03 |
| Behaviour IDs | B-15 |
| Priority | High |
| Design status | BLOCKED — REQUIREMENT UNCLEAR |
| Open question | Q-02 |
| Preconditions | Cart item at quantity 1; Q-02 resolved |
| Test data | -1 |
| Steps | 1. Enter -1. 2. Commit. 3. Inspect message, quantity and totals. |
| Expected result | Negative quantity is rejected; previous valid quantity and totals remain; validation explains the restriction. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-036 — Fractional quantity rejected

| Field | Value |
|---|---|
| Requirement | REQ-CART-03 |
| Behaviour IDs | B-16 |
| Priority | High |
| Design status | BLOCKED — REQUIREMENT UNCLEAR |
| Open question | Q-02 |
| Preconditions | Cart item at quantity 1; Q-02 resolved |
| Test data | 1.5 |
| Steps | 1. Enter 1.5. 2. Commit. 3. Inspect message, quantity and totals. |
| Expected result | Fractional quantity is rejected; previous valid quantity and totals remain; validation explains whole-number restriction. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-037 — Registration email lacks at sign

| Field | Value |
|---|---|
| Requirement | REQ-REG-03 |
| Behaviour IDs | B-22 |
| Priority | High |
| Design status | ASSUMED — confirm requirement before execution |
| Open question |  |
| Preconditions | Fresh logged-out session; approved fake registration dataset recorded; all fields except the target are valid; unique email |
| Test data | Email abc.com; other fields valid |
| Steps | 1. Fill form using abc.com. 2. Submit. |
| Expected result | Email validation explains invalid format; registration is prevented. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-038 — Extremely old date of birth policy

| Field | Value |
|---|---|
| Requirement | REQ-REG-05 |
| Behaviour IDs | B-26 |
| Priority | Low |
| Design status | BLOCKED — REQUIREMENT UNCLEAR |
| Open question | Q-04 |
| Preconditions | Fresh logged-out session; approved fake registration dataset recorded; all fields except the target are valid; unique email |
| Test data | 1900-01-01 (extreme value; not a known boundary) |
| Steps | 1. Enter DOB with other fields valid. 2. Submit. |
| Expected result | TBD: record accepted/rejected outcome and expected validation from Q-04. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-039 — Invalid checkout postcode policy

| Field | Value |
|---|---|
| Requirement | REQ-CHK-02 |
| Behaviour IDs | B-33 |
| Priority | Medium |
| Design status | BLOCKED — REQUIREMENT UNCLEAR |
| Open question | Q-05 |
| Preconditions | Address step; country selected; other fields valid |
| Test data | &lt;postcode violating confirmed country-specific rule&gt; |
| Steps | 1. Fill address except postcode. 2. Enter recorded invalid postcode. 3. Continue. |
| Expected result | TBD: confirm postcode validation is required and specify the expected message and blocked progression. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-040 — Invalid contact email rejected

| Field | Value |
|---|---|
| Requirement | REQ-CONT-02 |
| Behaviour IDs | B-37 |
| Priority | Medium |
| Design status | READY — requirement reviewed |
| Open question |  |
| Preconditions | Other required contact fields valid |
| Test data | Email abc; other fields recorded valid |
| Steps | 1. Fill contact form with abc as email. 2. Submit. |
| Expected result | Email format error is visible and submission is prevented; no success confirmation. |
| Actual result | Otherwise populated contact form with email abc displayed Email format is invalid; no success confirmation. Correcting only email later allowed successful submission. |
| Status | PASS |
| Data used | Contact: Portfolio Tester; portfolio-test@example.com (abc for negative case); Customer service; message: Disposable QA portfolio practice message for contact form validation only. No reply required. Registration: all fields blank. |
| Environment / date | 2026-11-01 Asia/Tbilisi; Windows host; in-app browser version/viewport unrecorded; UI v2.5 build 2026-10-11 |
| Notes / evidence | Execution recorded in execution-log.csv; no dedicated screenshot required. |
| Bug ID |  |

## TC-041 — Filter by one brand

| Field | Value |
|---|---|
| Requirement | REQ-FILT-01 |
| Behaviour IDs | B-10 |
| Priority | Medium |
| Design status | ASSUMED — confirm requirement before execution |
| Open question |  |
| Preconditions | Brand membership of sample products recorded |
| Test data | &lt;existing brand label&gt;; &lt;known member IDs&gt; |
| Steps | 1. Clear filters. 2. Select brand. 3. Inspect results across pages. |
| Expected result | Known brand members are present; all returned products belong to the selected brand. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-042 — Valid checkout reaches payment stage

| Field | Value |
|---|---|
| Requirement | REQ-CHK-03 |
| Behaviour IDs | B-34 |
| Priority | High |
| Design status | ASSUMED — confirm requirement before execution |
| Open question |  |
| Preconditions | Valid test account, available product and valid fake address prepared; checkout sequence confirmed |
| Test data | &lt;existing product selected during execution&gt;; record ID, name, URL, unit price and currency; quantity 1; &lt;valid fake billing/address dataset&gt; |
| Steps | 1. Log in. 2. Start with empty cart. 3. Add selected product. 4. Start checkout. 5. Complete required non-payment steps using recorded data. 6. Continue to payment stage. 7. Stop before submitting payment or placing an order. |
| Expected result | Payment stage is reachable; order summary retains product, quantity and calculated total. No payment is submitted. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-043 — Cart addition compatibility in Chrome and Firefox

| Field | Value |
|---|---|
| Requirement | REQ-COMP-01 |
| Behaviour IDs | B-42 |
| Priority | High |
| Design status | ASSUMED — confirm requirement before execution |
| Open question |  |
| Preconditions | Both browsers installed; versions recorded; empty cart in each run |
| Test data | &lt;existing product selected during execution&gt;; record ID, name, URL, unit price and currency; 1366x768; 100% zoom |
| Steps | 1. Execute TC-011 independently in Chrome and Firefox, resetting cart before each. 2. Record separate execution rows. |
| Expected result | Both browsers independently satisfy TC-011 expected result. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-044 — Checkout compatibility in Chrome and Firefox

| Field | Value |
|---|---|
| Requirement | REQ-COMP-01 |
| Behaviour IDs | B-43 |
| Priority | High |
| Design status | ASSUMED — confirm requirement before execution |
| Open question |  |
| Preconditions | Both browsers installed; separate valid checkout setups |
| Test data | &lt;existing product selected during execution&gt;; record ID, name, URL, unit price and currency; valid fake address; 1366x768 |
| Steps | 1. Execute TC-042 independently in Chrome and Firefox. 2. Record separate execution rows. 3. Stop before payment submission. |
| Expected result | Both browsers independently satisfy TC-042 expected result. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |

## TC-045 — Punctuation-only search policy

| Field | Value |
|---|---|
| Requirement | REQ-SRCH-01 |
| Behaviour IDs | B-06 |
| Priority | Medium |
| Design status | BLOCKED — REQUIREMENT UNCLEAR |
| Open question | Q-01 |
| Preconditions | Q-01 resolved |
| Test data | '-- |
| Steps | 1. Clear filters. 2. Enter literal punctuation input. 3. Submit. |
| Expected result | TBD: specify exact result set and message from Q-01. |
| Actual result | NOT EXECUTED |
| Status | NOT EXECUTED |
| Data used | TBD at execution |
| Environment / date | NOT EXECUTED |
| Notes / evidence | NOT EXECUTED |
| Bug ID |  |
