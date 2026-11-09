# HTTP/API basics

Request = method + URL + headers + optional body. Response = status + headers + optional body. Inspect protocol response and resulting UI/business state.

| Method | Common intent | Exercise constraint |
|---|---|---|
| GET | Retrieve a representation | Read-only product lookup after endpoint discovery |
| POST | Submit data for processing; often create a resource | Wrong-password login after contract review |
| PUT | Create/replace state at target resource, per contract | Design only unless disposable owned resource is available |
| PATCH | Apply partial changes | Confirm supported patch format |
| DELETE | Request removal of target resource association | Disposable owned test data only; never shared catalogue items |

| Code | Meaning | What to check |
|---|---|---|
| 200 | OK | Body and business result match contract |
| 201 | Created | Expected resource created; identifier/location if specified |
| 204 | No Content | No response content; verify intended state change separately |
| 400 | Bad Request | Request could not be processed as sent; inspect details |
| 401 | Unauthorized | Missing/invalid authentication credentials; inspect challenge/contract |
| 403 | Forbidden | Server refuses request; authentication alone may not resolve it |
| 404 | Not Found | Target absent or not disclosed; check endpoint and resource ID |
| 500 | Internal Server Error | Unexpected server condition; investigate request and reproducibility without asserting root cause |

HTTP-level success does not automatically mean the business operation behaved correctly. A 200 response may contain an application error or incorrect data. A 500 response should be investigated rather than automatically assuming the exact root cause.

These meanings are fundamentals, not predictions of Toolshop responses. Expected endpoint, status and schema must come from a verified contract. Other codes such as 422 may be specified; do not force a 400 expectation.

## Planned exercises

1. Find actual API documentation via the application or official project; record URL/version and supported endpoint. No API base URL is assumed.
2. GET product list: verify documented status, shape and required fields; compare an item with UI.
3. GET an ID confirmed absent: verify documented missing-resource outcome.
4. POST wrong-password login: verify documented error and absence of authenticated state; redact credentials.
5. Draft PUT/PATCH/DELETE requests for a disposable owned resource only if a suitable operation exists. Otherwise mark blocked and explain.
6. Use [execution log](api-test-log.md) for actual requests, responses, verdicts and evidence. None has run.

Reference terminology: RFC 9110 (HTTP Semantics) and RFC 5789 (PATCH). Read the API contract before choosing a verdict.
