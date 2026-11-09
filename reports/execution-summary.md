# Final execution summary

| Metric | Result |
|---|---|
| Designed | 45 |
| Executed (PASS + FAIL) | 18 |
| PASS | 16 |
| FAIL | 2 |
| Execution BLOCKED | 0 |
| NOT RUN | 27 |
| Pass rate | 88.89% of executed cases |
| Verified defects | 2 |

Execution: 2026-11-01, Asia/Tbilisi. Windows host; ChatGPT in-app browser. Exact browser engine/version and viewport were not recorded. Application title v5.0; visible footer v2.5, Built 2026-10-11, Angular 20.0.5. Shared demo data changed during testing, so product IDs are specific to each recorded run.

Completed coverage: homepage/product details; exact-name and no-result search; ascending prices across five pages; Hand Saw category filter including returned product membership; cart addition, badge and item presence; valid registration and required fields; password validation; all four designed login/session cases; all three contact-form cases. Console investigation was performed using captured browser logs.

Findings: BUG-001 (High/High) — quantity 3 shows line $42.45 and grand total $14.15, with quantity reset on refresh. BUG-002 (Medium/Medium) — password help says 8 characters while rejection message says 6. Backend root cause, exact accepted minimum password length and final charged amounts were not established.

Limited/unexecuted: cart removal and invalid quantities, brand filter, remaining registration negatives/DOB, full navigation and visual checks, checkout assertions through payment, complete mobile/tablet responsive cases, second-browser comparisons and API exercises. Checkout reached billing address while authenticated; an empty billing form had a disabled continue control, but full field-by-field TC-027 criteria were not completed. No payment was submitted.

Network capture: NOT EXECUTED. Second browser: NOT EXECUTED — unavailable through the browser connector used for these runs. Responsive viewports: no completed formal cases or recorded dimensions. API, Storage and real regression/retesting: NOT EXECUTED. These coverage gaps are separate from attempted-case blockers; no general execution blocker was established.

Conclusion: a partially executed manual QA portfolio with traceable outcomes and two reproducible defects. It demonstrates the recorded scope only and provides no release-readiness conclusion. Latest unique-case statuses define counts; repeat attempts remain in history and do not inflate the total.
