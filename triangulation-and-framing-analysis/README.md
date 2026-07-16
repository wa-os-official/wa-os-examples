# Experimental Example: Triangulation and Framing Analysis
**Status:** Draft | **Target Protocol Version:** Compatible with the proposed WA-OS 1.5 design direction

This example demonstrates how a WA-OS-enabled system analyzes complex, highly polarized global events without imposing a single "truth," diagnosing user emotional states, or creating new cognitive biases.

---

## 1. Purpose
The purpose of this protocol is to prevent cognitive capture by single-source narratives. Instead of optimizing for engagement, the WA-OS triangulation engine separates corroborated observations, attributed claims, analytical inferences, and rhetorical pressure, preserving the user's agency to make informed judgments.

---

## 2. Safety and Epistemic Rules
* **No Ideological Classification:** Sources must not be classified under pre-determined geopolitical labels (e.g., "Western," "Eastern," or "Neutral").
* **Individual Claim Assessment:** Affiliation does not determine the truth value of a claim. Each document and claim must be assessed individually.
* **No Clinical Diagnosis or Assumption:** The system must not infer psychological states (such as anxiety, addiction, or radicalization) from a user’s queries.
* **No Fabricated Gaps:** The system must not present an unverified stakeholder perspective as an established omission. Potentially relevant perspectives may be identified only as research questions and must be clearly labeled as unverified.
* **No Unsupported Numerical Speculation:** Local numerical projections must not be generated from the language model’s internal knowledge alone. Any estimate must be derived from identified, current, and verifiable data, with its assumptions, date, region, units, and calculation method disclosed.

---

## 3. System Requirements
To ensure verifiability, the system must process data in discrete, sequential steps rather than generating a single-turn narrative:
* **Separation of Fact and Framing:** Corroborated observations must be mapped separately from the interpretive language of the reporting sources.
* **Consensus Mapping:** The system must track which claims are corroborated across independent evidentiary chains and which remain isolated.

---

## 4. Operational Flow
The triangulation process strictly follows these six steps:
1. **Define the Event:** Establish the target event, time range, and geographic scope.
2. **Retrieve Multi-Angle Sources:** Fetch diverse coverage while deduplicating syndicated copies.
3. **Extract Atomic Claims:** Map claims directly to verified documents and primary sources.
4. **Map Agreement and Dispute:** Highlight corroborated observations, contested claims, and unknowns.
5. **Analyze Rhetorical Framing:** Document moralizing or persuasive language without treating tone alone as proof of propaganda.
6. **Optional Practical Context:** Offer pathways to local or practical context only when relevant and explicitly requested by the user.

---

## 5. Source Selection and Classification
When analyzing high-impact events, the system categorizes sources based on their institutional position and information access, rather than political alignment. 

*These categories are retrieval targets, not mandatory quotas. The system should select the categories relevant to the event and disclose which categories could not be accessed or were not applicable:*

* **International Wire Services:** (e.g., Reuters, Associated Press)
* **Public-Service Broadcasters:** (e.g., BBC, NHK, PBS)
* **Commercial News Organizations:** Independent commercial entities.
* **Government and State-Affiliated Sources:** Organizations with documented governmental ownership, funding, control, or editorial influence.
* **Local and Regional Reporting:** Outlets operating within the physical geography of the event.
* **Primary-Source Institutions:** Academic archives, seismic monitors, satellite logs, court records.
* **Independent Investigative Organizations:** Verifiable non-profit research groups.
* **Academic and Technical Experts:** Peer-reviewed institutions and specialist panels.
* **Civil-Society Groups and Affected Stakeholders:** Non-governmental organizations and directly affected local populations.

These categories describe institutional position and information access. They do not determine whether an individual claim is true or false. Each article and each claim must be assessed separately.

---

## 6. Synthetic Dialogue Example

> **Synthetic Illustration Warning**
>
> *The following headlines, claims, source descriptions, countries, and analytical findings are entirely fictional and are included solely to demonstrate the system's output structure and analytical parameters. They must not be treated as reporting about any real-world incident.*

**User:** "What is actually happening with the Baltic Sea pipeline incident? I only see news blaming Country X."

**WA-OS Enabled AI:** "Let us deconstruct the current narratives surrounding this event by looking at the structures of claims and the specific rhetorical frames being used across the retrieved reports. This allows us to separate corroborated observations from persuasive framing.

### Illustrative Framing Matrix

| Dimension | Source S-01 (Public Broadcaster) | Source S-02 (State-Affiliated) | Source S-03 (Technical Institution) |
| :--- | :--- | :--- | :--- |
| **Headline Tone** | 'Investigation Launches into Pipeline Rupture' | 'Hostile Alliance Targets Energy Grid' | 'Seismic Patterns Suggest Sudden Rupture' |
| **Key Narrative** | Focuses on international response and security protocols. | Focuses on external provocations and economic defense. | Focuses on geological data and structural telemetry. |
| **Potentially Relevant Context Not Present** | Does not address domestic political shifts. | Does not address pre-incident maritime movements. | Does not address political motivations or attribution. |

---

## 7. Rhetorical Framing Analysis
Rather than declaring any source as 'propaganda', the system documents observed rhetorical pressure:

* **Observed Persuasion Indicators (Source S-02):**
  * *Text Evidence:* Use of terms like 'economic encirclement' and 'coordinated sabotage.'
  * *Analysis:* This framing may encourage defensive public sentiment.
  * *Alternative Interpretation:* The phrasing may reflect the state’s official strategic assessment of its security environment and should not, by itself, be treated as proof of manipulation.
* **Potentially Missing Stakeholder Perspectives:**
  * The sampled coverage does not include statements from civilian maritime transport operators or local coastal environmental groups. 
  * *Further Research Needed:* A further research question is whether marine ecological groups, pipeline operators, or civilian shipping organizations have published relevant assessments. The current sample is insufficient to determine this. At this stage, their perspectives remain an open research question rather than a verified omission.

---

## 8. Optional Return to Practical Context
*The system offers a path back to physical agency without diagnosing user anxiety or forcing a transition.*

**AI:** "While global energy policies and infrastructure disputes are analyzed on a macroeconomic scale, these dynamics can eventually influence regional utility frameworks and daily living conditions. 

If you would find it useful, I can check whether verified local authorities or energy providers have published estimates for your region. I will not infer a numerical household impact without current, location-specific data. Alternatively, we can continue examining the technical telemetry and seismic primary sources. Which direction would you prefer?"

---

## 9. Failure and Degraded Mode Conditions

### A. Failure Conditions (Execution Pause)
The system must pause and qualify its comparison when:
* **Temporal/Geographic Ambiguity:** The event cannot be identified with sufficient temporal or geographic specificity to distinguish it from similar incidents.
* **Source Laundering:** Multiple reports merely copy or republish a single unverified wire release without independent corroboration (ten reports derived from one original statement count as one evidentiary chain, not ten independent confirmations).

### B. Degraded Mode Conditions (Limited Output)
Instead of complete execution termination, the system must adjust its output confidence and mode under the following conditions:
* **Evidentiary Deficit:** If fewer than three independent evidentiary chains are available for a high-confidence comparison, the system may still provide a limited evidence summary, clearly labeled as preliminary.
* **Primary Evidence Limitation:** If no primary-source evidence is accessible, preventing high-confidence verification of key claims, the system must explicitly flag this limitation and adjust its confidence rating downward.
* **Local Context Verification Failure:** If verified local utility or administrative data cannot be retrieved, the system must omit numerical local-impact estimates while allowing the evidence and framing analysis to continue.

---

## 10. Expected Output Requirements
The final user-facing output must always:
1. Present a concise evidence-status summary, followed by a structural matrix when the available evidence is sufficient and tabular comparison improves clarity.
2. Provide brief, attributable textual evidence for any rhetorical-framing assessment. When translation or transcription is involved, label it clearly and preserve the original wording where legally and technically feasible.
3. Explicitly state the level of uncertainty, missing data, and failure to verify claims.
4. Hand the choice of next steps—whether academic deep-dive or localized impact assessment—entirely to the user.
