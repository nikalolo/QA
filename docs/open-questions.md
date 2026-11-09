# Requirement clarification log

These are design blockers, not executed blocked results. TC-004 was scoped to an exact-name assumption and executed; TC-019 exposed BUG-002. Other question-dependent cases remain NOT EXECUTED. Do not choose whichever outcome the app happens to return as the test oracle.

| ID | Question | Affected tests | State | Answer / source / date |
| --- | --- | --- | --- | --- |
| Q-01 | Search matching fields, case rules, empty input and literal/special input policy | TC-004, TC-006, TC-007, TC-045 | TO BE VERIFIED | TBD |
| Q-02 | Quantity MIN/MAX, stock cap, zero-as-remove policy, decimal/negative rejection and exact retained cart state | TC-013, TC-014, TC-035, TC-036 | TO BE VERIFIED | TBD |
| Q-03 | Password length/composition rules and validation messages | TC-019 | TO BE VERIFIED | TBD |
| Q-04 | DOB permitted range, future dates, minimum/maximum age and timezone | TC-021, TC-038 | TO BE VERIFIED | TBD |
| Q-05 | Whether postcode validation exists and country-specific accepted/rejected formats | TC-039 | TO BE VERIFIED | TBD |

For each resolution, record source, rationale and affected requirement/case edits. If no intended rule is available, report observed behaviour without PASS/FAIL; keep the design blocked. Other assumptions still require review even when not listed here.
