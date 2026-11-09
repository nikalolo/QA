# Editing and execution

`test-cases.csv` is the editable source of truth for definitions and the latest recorded result per case. `test-cases.md` and `docs/04-traceability.md` are generated views: do not edit them directly. `docs/behaviour-map.csv` is the editable behaviour-to-case map.

Run with Python 3.10+ from any directory:

```sh
python /path/to/toolshop-qa-portfolio/test-cases/generate.py
python /path/to/toolshop-qa-portfolio/test-cases/generate.py --check
python /path/to/toolshop-qa-portfolio/test-cases/test_generate.py
```

On Windows, quote paths containing spaces and use your installed Python executable. No third-party packages required. This is documentation/data-generation tooling, **not test automation**.

The generator only writes the two generated Markdown views. It never writes CSV source, execution history, bugs or evidence. `--check` is read-only and rejects stale views, duplicate IDs, invalid mappings or malformed execution states. Keep CSV in UTF-8; quote cells with commas/newlines. Commit definition changes before running tests so old outcomes remain interpretable.

## Record real execution

- `Design status`: ASSUMED until the oracle is reviewed; `BLOCKED — REQUIREMENT UNCLEAR` when a question prevents a verdict. After resolution use `READY — requirement reviewed` with source in notes.
- `Status`: exactly NOT EXECUTED, PASS, FAIL or BLOCKED. Unattempted tests retain Actual result = NOT EXECUTED. An execution blocker differs from a design blocker.
- For an actual run fill actual result, exact data used, environment/date and notes/evidence. Do not store secrets. Bug ID stays empty unless a genuine defect report exists; a FAIL can be under investigation.
- Append one row per actual attempt to `execution-log.csv`, with unique Run ID, case revision, environment and purpose (initial, compatibility, regression or retest). The file starts with headers only: no fake executions.
- For parameterized page/browser checks, record sub-results in history. Mark the parent PASS only when all required checks passed; FAIL if any assertion failed, BLOCKED if unfinished with no failure. A single browser success is insufficient for a two-browser case.
- Preserve earlier history before updating the latest CSV result. Do not count repeated runs as new designed cases. Summary metrics use latest case status; report environment coverage separately.

A new case needs a stable new ID and a behaviour-map entry. Never renumber existing IDs. For definition changes after execution, preserve prior outcome/history and explicitly reset the current outcome for the new revision. The generator does not infer this decision.
