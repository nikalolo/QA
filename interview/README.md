# Interview notes grounded in this project

Speaking prompts, not claims of completed testing.

| Question | Short answer |
|---|---|
| Scenario vs case vs checklist? | Checkout reaches payment is a scenario; TC-042 specifies setup, steps and expected result; the exploratory checklist guides discovery. |
| Severity vs priority? | Severity is impact; priority is urgency. The hypothetical cart example distinguishes incorrect checkout amounts from display-only errors. |
| Smoke, sanity, regression, retesting? | Smoke checks critical availability/login. Sanity focuses on a small change (team definitions vary). Regression checks related behaviour; retesting repeats failed steps after a fix. |
| Equivalence partitioning? | Negative whole quantities and fractions are separate invalid classes in TC-035/TC-036. |
| Boundary values? | I need confirmed MIN/MAX. 999999 is an extreme input, not a verified boundary. |
| Expected results? | I describe observable assertions, such as quantity × unit price, and record their rule. “Handled gracefully” cannot produce a reliable verdict. |
| Unclear requirements? | Log a question and block the design decision; exploration can record behaviour without calling it correct. Unresolved questions remain in the clarification log. |
| Network tab? | Method, URL, headers, query/payload, status, response and timing. Correlate with UI action and redact secrets. Console investigation was performed; Network exercises remain unexecuted. |
| Is HTTP 200 a pass? | I still inspect data and business effect. A 500 needs investigation and does not identify root cause. |
| Bug lifecycle? | Record symptom/impact, triage, link fix, retest, close or reopen. Two verified reports show cart totals and password-guidance problems. |
| Regression selection? | For simulated quantity changes: invalid quantities/totals, cart and checkout dependencies, then smoke/browser checks as planned. No run is claimed. |
| Risk-based testing? | Account access, cart totals and checkout are High because failures interrupt core tasks. Unknown rules/shared data are risks. |
| Compatibility vs responsive? | Check functional criteria independently in Chrome/Firefox; inspect layout/navigation at 375/768 CSS-pixel widths. |
| Emulation vs real device? | Emulation helps with breakpoints, but does not establish physical touch, keyboard or actual mobile-browser behaviour. |
| Project design? | Reviewed 34 unexecuted cases, isolated inputs, added brand/payment-stage coverage and linked behaviours to cases. Now 45 designed cases, 18 executed. |
| Is generate.py automation? | It generates documentation from CSV; it does not test the application. |

## Honest portfolio wording now

“Prepared a manual QA portfolio for Toolshop with 45 test cases, draft requirements, behaviour-level traceability, bug-report templates, and planned DevTools, browser and regression exercises. Executed 18 cases: 16 PASS, 2 FAIL, with two verified defects; remaining coverage is disclosed.”

After real work, replace planning language only where supported by runs/evidence. Explain what you personally executed and any assistance used; be ready to discuss one case and its rationale.

## Internship skill → artifact

Requirements: requirements/open questions. Test design: CSV/design notes. UI/mobile/browser planning: matrix and cases. Bug workflow/retest: templates/lifecycle. HTML/CSS/DevTools: exercises. HTTP: fundamentals/log. Reporting: history/summary. Tracker familiarity: proposed Trello workflow only.
