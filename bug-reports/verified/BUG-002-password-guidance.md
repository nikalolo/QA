# BUG-002: Registration password validation contradicts displayed length guidance

Status New; severity Medium; priority Medium. Validation blocks account creation but provides misleading correction instructions. No security weakness or exact backend rule is asserted.

Environment: 2026-11-01 Asia/Tbilisi; Windows host; ChatGPT in-app browser, exact engine/version/viewport unrecorded; UI v2.5 Built 2026-10-11 Angular 20.0.5. URL /auth/register.

Preconditions: logged out, registration form open. Steps: read help; submit empty form; compare password messages. Repeat on fresh form. Populate remaining registration fields with synthetic data and a six-character password containing uppercase/lowercase/number/symbol; submit. Expected: help and validation communicate the same length requirement. Actual: help says at least 8 characters, validation says minimal 6 characters. Six-character mixed password was rejected with that message; longer mixed password allowed registration. Exact minimum and all accepted lengths were not established. Official specification was not verified.

Reproducibility: contradiction observed in prior session and fresh registration form; isolated six-character submission also showed misleading message. Related REQ-REG-03 / TC-019. Password values are omitted.

Evidence: [guidance screenshot](../../evidence/screenshots/bugs/BUG-002-password-guidance.png). Registration success: [new identity](../../evidence/screenshots/test-execution/registered-account.png). No Network evidence. Not related to BUG-001.
