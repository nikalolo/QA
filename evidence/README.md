# Execution evidence and collection guidance

Collect meaningful evidence for defects, uncertain behaviour, key checkout/cart checks, layout differences and technical investigations. A screenshot is not required for every passing test.

Folders under `screenshots/`: `bugs/`, `test-execution/`, `responsive/`, `cross-browser/`, `devtools/`, `api/`. Text/network extracts may sit beside screenshots. Empty `.gitkeep` files preserve folders; they are not evidence.

Filename pattern: `TC-042_RUN-001_chrome-<version>_<YYYY-MM-DD>_payment-stage.png` (fill real values). Bugs use real BUG IDs; exercises use DT/API IDs. Add a sequence suffix for multiple files. Link relative paths from run/report records.

Capture page, trigger and observed result; record URL/build, exact browser/OS, viewport, data aliases and actual capture time in the run. Before/after totals help calculation defects; paired viewport images help responsive issues. Physical-device evidence must name the actual device.

Remove passwords, tokens, authorization/cookie values, personal data and unrelated tabs. HAR files/payloads may contain secrets; review exported content. Keep redaction clear and preserve the symptom. Never manufacture or edit an image to change observed behaviour.
