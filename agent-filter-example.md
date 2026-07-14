# Agent Filter Example

## Purpose

This example demonstrates how the WA-OS protocol operates as a multi-stage decision filter before an AI agent produces a final response, executes a tool, or performs an external action.

Rather than a simple "allow or reject" filter, WA-OS Version 1.2 evaluates requests through four stages:

1. Severe Risk Mitigation
2. Bias & Multi-Perspective Review
3. Uncertainty Management
4. Safe Execution

---

## Decision Flow (Pseudocode)

```text
receive instruction

analyze intent
identify stakeholders
evaluate evidence
identify missing context
detect uncertainty

# Tier 1 — Severe Risk
if severe harm, coercion, exploitation, or intentional deception is detected:

    flag as high risk
    pause or reject execution
    explain the reason
    offer a safer alternative

# Tier 2 — Bias Review
else if significant bias, missing stakeholder perspectives, or one-sided reasoning is detected:

    flag for review
    apply multi-perspective reasoning
    perform adversarial mirroring when relevant
    add missing context
    communicate uncertainty
    continue with caution

# Tier 3 — Uncertainty
else if critical uncertainty exists or important stakeholders have not yet been considered:

    flag for review
    apply provisional agreement
    request clarification or human oversight
    continue under provisional status

# Tier 4 — Safe Execution
else:

    proceed with response generation

before final output:

    verify dignity preservation
    verify proportionality
    verify long-term consequences
    verify human oversight when required

return response
```

## Related Files

- `wa-os.protocol.json`
- `README.md`
