# Observed feature inventory

Observed 2026-11-01 in the in-app browser, UI footer v2.5 Built 2026-10-11. Observations describe actual behaviour, not confirmed intended requirements.

| Module / page | Inputs and observed behaviour | Dependencies / validation | Questions / evidence |
|---|---|---|---|
| Home / | Catalogue, categories/brands, price range and sort controls visible | Shared catalogue can change | TC-001; homepage screenshot |
| Search / | Exact Combination Pliers returns one matching item; zzzzqqq returns zero and no-results message | No filters selected | Broader Q-01 matching/empty-input policy unresolved; TC-004/005 |
| Sort / | Price Low-High is nondecreasing across five pages | Same live catalogue | TC-008; price-sort-pages.txt |
| Category / | Hand Saw returns Wood Saw; details show Hand Saw | Clear other filters | TC-009; brand filter not formally verified |
| Product /product/... | Combination Pliers $14.15; description and add control. Wood Saw $12.18, Hand Saw, ForgeFlex Tools | Availability varies | TC-010; runtime IDs in execution records |
| Cart /checkout | Add one Wood Saw: badge 1, line $12.18; eco discount $0.61, total $11.57 | Cart setup/session | TC-011; BUG-001 affects quantity recalculation/persistence |
| Registration /auth/register | Required-field messages; synthetic account created and login identified Portfolio Tester | Address lookup may replace entered fields | BUG-002; exact password minimum and DOB range unresolved |
| Login/profile | Demo login works; wrong password rejected; protected profile redirects to login after logout/Back/reload | Valid demo credentials; secrets excluded | TC-022–TC-025 |
| Checkout /checkout | Cart → sign-in → billing reached; empty billing continue disabled | Authenticated session/address fields | Payment-stage path not completed; Q-05 unresolved |
| Contact /contact | Required fields and invalid email validated; valid synthetic submit confirmed | Subject and message required | TC-028/029/040; delivery not asserted |
| Responsive / compatibility | No completed formal responsive/second-browser run | Exact viewport/version not recorded | NOT EXECUTED |
