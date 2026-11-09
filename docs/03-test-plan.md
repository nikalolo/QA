# Manual test plan

Owner: Nika (GitHub: nikalolo), QA internship portfolio. Status: partial real execution completed; current outcomes in reports/execution-summary.md.
Target: https://practicesoftwaretesting.com — exact variant/build TO BE VERIFIED. Independent learning project.

## Scope and approach

In scope: navigation, search, category/brand filtering, price ascending sort, product details, cart, registration, login/logout, contact, checkout through the payment stage, UI review, responsive emulation, Chrome/Firefox compatibility, basic DevTools and HTTP exercises.
Out of scope: payment submission, real transactions, admin, penetration/security testing, load/performance testing, full accessibility audit and automated application tests.

Use detailed cases for repeatable functional checks; timeboxed exploration to learn the application and expose gaps; separate browser/viewport runs for compatibility and responsiveness. Simulated regression selection is planning only. Retesting repeats a real defect after a known fix.

## Environment and entry criteria

Record URL/variant/build (or `not exposed` plus actual observation date), OS, exact browser version, viewport in CSS pixels, zoom, account alias and data setup. Planned desktop viewport: 1366x768; emulation: 375x667 and 768x1024. Optional physical phone: model, OS, browser version and orientation. No environment has been tested yet.

Before each case: app reachable, approved expected result, required dataset available, setup reset, and evidence destination ready. Resolve its open questions first. If intended behaviour cannot be established, keep design blocked; exploration may record observations without a verdict.

## Execution workflow

1. Confirm the case definition and record its revision/build context.
2. Run exact steps with recorded values; evaluate every expected assertion.
3. Store current outcome in the CSV and append a history row for each browser, data iteration, retest or regression run. Never replace earlier history.
4. Investigate unexpected behaviour against the requirement before calling it a verified defect.
5. Regenerate Markdown/traceability views and update the execution summary.

Use [execution instructions](../test-cases/README.md). PASS/FAIL require an actual observed result; BLOCKED records an attempted run prevented by setup or unresolved requirements. Planning blockers live separately in `Design status`.

## Risks and completion criteria

Highest risks: incorrect cart totals, account access, checkout progression. Public data may reset, shared accounts can interfere, and intended requirements are unavailable. Use fake data and document resets.

Proposed target: execute all High-priority cases and at least 90% of the detailed suite; account for every remaining case and investigate every failure. Report unresolved blockers and serious defects, browser/device gaps, and incomplete requirement decisions. Failing to meet the target means incomplete testing. Completion of this portfolio does not authorize a product release.
