# BUG-001: Cart grand total is not recalculated after quantity increase

Status: New. Observed 2026-11-01 Asia/Tbilisi. Environment: Windows host; ChatGPT in-app browser (exact browser version and viewport unavailable). URL: https://practicesoftwaretesting.com/checkout. UI footer: v2.5, Built 2026-10-11, Angular 20.0.5.

Preconditions: fresh temporary browser session, logged out, no cart indicator initially. Test data: Combination Pliers, unit price $14.15, quantity initially 1; current live dataset changed product IDs during the session, so use the visible name and price. No other cart lines.

## Reproduction

1. Open home, open Combination Pliers, add quantity 1.
2. Open cart; confirm quantity 1, line $14.15 and grand total $14.15.
3. Replace quantity with 3 and press Tab.
4. Observe line $42.45 but grand total $14.15.
5. Refresh; quantity returns to 1.
6. Repeat quantity 3 using Enter; same mismatch.

Expected: quantity 3 yields line and grand total $42.45 with one line and no adjustments, per REQ-CART-02 and independent multiplication. Actual: line recalculates, grand total remains $14.15; quantity is not retained after refresh.

Reproducibility: 2/2 focused attempts in this session (Tab and Enter), plus earlier recorded reproductions. Severity: High: incorrect displayed checkout cart amount and inconsistent quantity state affect the purchase flow. Priority: High: core cart functionality. No final payment/order was submitted; incorrect charged amount is NOT established.

Related requirement: REQ-CART-02. Related case: TC-012. Screenshot: [mismatch](../../evidence/screenshots/bugs/BUG-001-grand-total.png). Console: [captured logs](../../evidence/screenshots/devtools/BUG-001-console.json).

Network inspection: request URL/method/status/payload/response NOT CAPTURED. Browser connector exposes Console logs but no Network capture method; native DevTools Network was not completed. Whether an update request is sent or the API returns quantity 3/$42.45 is unknown. Do not infer frontend/backend root cause from refresh or Console symptoms. The null cart_items errors remain a separate investigation; causal relationship unproven.
