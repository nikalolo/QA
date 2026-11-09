# Exploratory session guide

Actual observations are in docs/01-feature-inventory.md; this reusable charter was not completed as a separate scored session.

Charter: learn the customer journey and identify missing rules, data dependencies and confusing feedback. Timebox: 60–90 minutes. Record actual session date/time, environment, scope, observations, evidence and questions. A checkbox means explored, not PASS.

- [ ] Map header/footer destinations; observe Back, Forward and reload transitions.
- [ ] Discover search matching, empty input and special-input handling; record Q-01 findings.
- [ ] Explore category and brand separately, then combined; inspect sorting across pages.
- [ ] Identify product availability, cart quantity rules and total calculation; investigate Q-02.
- [ ] Identify registration mandatory fields, password rules and DOB limits; investigate Q-03/Q-04.
- [ ] Observe login errors, logout and protected-page access with fake credentials.
- [ ] Follow checkout to payment stage and stop; identify address/postcode rules (Q-05).
- [ ] Identify contact fields, message limits and submission feedback.
- [ ] Inspect validation recovery and retained non-secret values.
- [ ] Inspect narrow layouts for overlaps, clipped text, unusable menus and controls.
- [ ] Observe Console/Network entries; distinguish expected validation errors from unexpected failures.

| Observation ID | Action / exact data | Observation | Environment | Evidence | Question / requirement | Next action |
|---|---|---|---|---|---|---|

Debrief: features discovered, unanswered rules, top three risks and proposed case changes. Keep observations distinct from confirmed requirements. Use detailed cases for repeatable verdicts; use this charter for discovery. For smoke/regression, select explicit case IDs rather than treating checked boxes as results.
