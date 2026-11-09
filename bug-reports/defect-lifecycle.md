# Defect lifecycle and triage

Proposed workflow: New → Investigating/Assigned → In Progress → Fixed → Ready for Retest → Closed. Reopen if the original failure remains. Record reasons for Duplicate, Rejected or Deferred. These are workflow definitions, not performed activity.

Check the requirement, data, build, network and reproducibility. Another browser/private session helps isolate conditions but is not mandatory before reporting. Browser-specific and intermittent defects can be genuine. Reproduction in another browser alone does not prove an app defect.

Severity describes impact; priority describes urgency. Explain both using affected flow, workaround and frequency. A cosmetic issue may be urgent for a public campaign; a severe rare issue still needs scheduling context.

Retesting: repeat original failing steps/data against a known fixed build and record a new run. Close only when verified; otherwise reopen with evidence. Regression: run related cases for unintended effects. A simulated change provides selection practice only, not a real fix or completed retest.
