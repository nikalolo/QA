# Regression selection and execution

## Selection exercise: SIMULATED change

Scenario only: cart quantity validation was changed. No actual change, fix, regression run or retest is claimed.

| Relationship | Selected cases | Reason |
|---|---|---|
| Directly affected | TC-012, TC-013, TC-014, TC-035, TC-036 | Quantity changes, invalid partitions and totals |
| Related cart state | TC-011, TC-015 | Addition/removal may share cart update logic |
| Downstream checkout | TC-026, TC-042 | Quantities/totals must reach checkout intact; stop before payment |
| Smoke | TC-001, TC-022 | App availability and account access |
| Browser follow-up | TC-043, TC-044 | Chrome/Firefox cart and checkout if validation/UI code changed |

Order: resolve relevant questions/setup; smoke; direct risk; downstream cart/checkout; browser coverage indicated by change. Add concrete MIN/MAX cases only after Q-02 resolution. Under time pressure prioritize incorrect totals and blocked checkout; record deferred cases and residual risk.

## Real-change execution template — NOT EXECUTED

Change ID/description/source: TBD. Previous/new build: TBD. Actual environment/period: NOT EXECUTED. Selected cases/rationale: TBD (selection above is hypothetical).

| Run ID | Case | Actual date / build / environment | Actual result | Status | Evidence / defect |
|---|---|---|---|---|---|

Selected count: TBD; executed/pass/fail/execution-blocked: 0/0/0/0; verified new defects: 0; conclusion: NOT EXECUTED. Link actual history and deferred coverage after a real run.

Retesting is separate: for a genuine fixed defect record Bug ID/fix build, repeat original failed steps/data, then close or reopen based on observation. Related regression passing alone does not verify the original bug fix.
