# Toolshop manual QA portfolio

Manual QA practice for the [Practice Software Testing Toolshop](https://practicesoftwaretesting.com) demo. Maintainer: Nika (nikalolo), QA internship candidate.

## Scope and testing performed

Customer browsing/search, price sorting, category filtering, product/cart checks, registration, login/logout/session protection and contact forms. Executed positive and negative functional checks, input partitions and Console investigation. Checkout exploration reached billing; payment submission is outside scope. Boundary design and regression selection are preparation only.

## Final results

| Designed | Executed | PASS | FAIL | BLOCKED | NOT RUN | Verified defects |
|---|---|---|---|---|---|---|
| 45 | 18 | 16 | 2 | 0 | 27 | 2 |

Pass rate: 88.89% of executed cases. This portfolio contains partial execution, not full application coverage.

## Best artifacts

- [Execution summary](reports/execution-summary.md)
- [Test cases](test-cases/test-cases.md) and [execution history](test-cases/execution-log.csv)
- [Requirements traceability](docs/04-traceability.md) and [test plan](docs/03-test-plan.md)
- [BUG-001 — cart total mismatch](bug-reports/verified/BUG-001-cart-grand-total.md), High severity/priority
- [BUG-002 — contradictory password guidance](bug-reports/verified/BUG-002-password-guidance.md), Medium severity/priority
- [Observed features](docs/01-feature-inventory.md), [Console evidence](devtools/exercises.md), [evidence guide](evidence/README.md)

## Environment and limitations

Executed 2026-11-01 (Asia/Tbilisi) using an in-app browser on a Windows host. Browser engine/version and viewport dimensions were not recorded; no completed formal responsive, physical-device or second-browser coverage is claimed. UI footer: v2.5, Built 2026-10-11, Angular 20.0.5. Demo data is shared and may reset.

Network capture and API execution were not performed. Cart removal, brand filtering, full checkout and remaining validation/visual cases remain NOT RUN. Requirements retain assumptions where no specification source exists. Screenshots and logs contain synthetic/demo data only; no saved passwords or tokens. Execution assistance does not substitute for being able to explain and reproduce portfolio work in an interview.

## Maintain the existing suite

CSV is authoritative. Run `python test-cases/generate.py`, `python test-cases/generate.py --check`, and `python test-cases/test_generate.py`. Standard-library documentation tooling; no application automation framework. [Tooling validation](reports/repository-health.md).
