# Multi-Agent Consensus & Validation Example

## Purpose
This example demonstrates how the WA-OS Protocol can be integrated as a governance and validation layer within a Multi-Agent system (e.g., CrewAI, AutoGen, or LangGraph). 

Instead of treating the validator as a simple "stop/go" binary switch, WA-OS acts as a cognitive harmonizer that handles risks, biases, and uncertainties through active negotiation.

---

## Agent Roles & Architecture

* **Agent A: Planner (The Optimizer)**
  * *Role:* Proposes strategies, steps, and actions to achieve specific tasks as efficiently as possible.
* **Agent B: Executor (The Operator)**
  * *Role:* Drafts responses, prepares API calls, or configures system changes.
* **Agent C: WA-OS Validator (The Harmonizer)**
  * *Role:* Intercepts proposals, applies the 4-tier evaluation pipeline (using `wa-os.protocol.json`), and either approves, contextualizes, proposes provisional agreements, or rejects the actions.

---

## Collaboration Flow (Negotiation & Alignment)

```text
[Agent A: Planner] ───────(Proposes Action)───────> [Agent B: Executor]
                                                           │
                                                   (Prepares Output)
                                                           │
                                                           ▼
                                                [Agent C: WA-OS Validator]
                                                           │
                                           ┌───────(Applies 4 Tiers)───────┐
                                           │                               │
                                    [High Risk]                     [Bias/Uncertainty]
                                           │                               │
                                   (Direct Reject)                 (Request Revision /
                                           │                        Inject Context)
                                           ▼                               │
                                 [Halt / Redirect]                         ▼
                                                                  [Collaborative Agreement]
