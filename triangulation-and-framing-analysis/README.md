# Experimental Example: Triangulation and Framing Analysis
**Status:** Draft | **Target Protocol Version:** Compatible with the proposed WA-OS 1.5 design direction

This example demonstrates how a WA-OS-enabled system analyzes complex, highly polarized global events without imposing a single "truth," diagnosing user emotional states, or creating new cognitive biases. 

---

## 1. Purpose
The purpose of this protocol is to prevent cognitive capture by single-source narratives. Instead of optimizing for engagement, the WA-OS triangulation engine separates confirmed facts, attributed claims, and rhetorical pressure, preserving the user's agency to make informed judgments.

---

## 2. Safety and Epistemic Rules
* **No Ideological Classification:** Sources must not be classified under pre-determined geopolitical labels (e.g., "Western," "Eastern," or "Neutral").
* **Individual Claim Assessment:** Affiliation does not determine the truth value of a claim. Each document and claim must be assessed individually.
* **No Clinical Diagnosis or Assumption:** The system must not infer psychological states (such as anxiety, addiction, or radicalization) from a user’s queries.
* **No Fabricated Gaps:** Missing perspectives must never be invented or assumed by the system.
* **No Numerical Speculation:** Any local numerical projections (e.g., energy costs, taxation) must be retrieved from verified local utility or government databases. Under no circumstances may the system synthesize or estimate these numbers.

---

## 3. System Requirements
To ensure verifiability, the system must process data in discrete, sequential steps rather than generating a single-turn narrative:
* **Separation of Fact and Framing:** Confirmed physical realities must be mapped separately from the interpretive language of the reporting sources.
* **Consensus Mapping:** The system must track which claims are corroborated across independent evidentiary chains and which remain isolated.

---

## 4. Operational Flow
The triangulation process must strictly follow these six steps:
1. **Define the Event:** Establish the target event, time range, and geographic scope.
2. **Retrieve Multi-Angle Sources:** Fetch diverse coverage while deduplicating syndicated copies.
3. **Extract Atomic Claims:** Map claims directly to verified documents and primary sources.
4. **Map Agreement and Dispute:** Highlight corroborated facts, contested claims, and unknowns.
5. **Analyze Rhetorical Framing:** Document moralizing or persuasive language without treating tone alone as proof of propaganda.
6. **Optional Practical Context:** Offer pathways to local or practical context only when relevant and explicitly requested by the user.

---

## 5. Source Selection and Classification
When analyzing high-impact events, the system categorizes sources based on their institutional position and access, rather than political alignment:
* **International Wire Services:** (e.g., Reuters, Associated Press)
* **Public-Service Broadcasters:** (e.g., BBC, NHK, PBS)
* **Commercial News Organizations:** Independent commercial entities.
* **Government and State-Affiliated Sources:** State-funded or directly controlled mouthpieces.
* **Local and Regional Reporting:** Outlets operating within the physical geography of the event.
* **Primary-Source Institutions:** Academic archives, seismic monitors, satellite logs, court records.
* **Independent Investigative Organizations:** Verifiable non-profit research groups.
* **Academic and Technical Experts:** Peer-reviewed institutions and specialist panels.
* **Civil-Society Groups:** Non-governmental organizations and directly affected local populations.

---

## 6. Synthetic Dialogue Example

> **Synthetic Illustration Warning:** > *The following headlines, claims, omissions, countries, and numerical values are entirely fictional and are included solely to demonstrate the system's output structure and analytical parameters. They must not be treated as reporting about any real-world incident.*

**User:** "What is actually happening with the Baltic Sea pipeline incident? I only see news blaming Country X."

**WA-OS Enabled AI:** "Let us deconstruct the current narratives surrounding this event by looking at the structures of claims and the specific rhetorical frames being used across the retrieved reports. This allows us to separate verified physical facts from persuasive framing.

### Illustrative Framing Matrix

| Dimension | Source S-01 (Public Broadcaster) | Source S-02 (State-Affiliated) | Source S-03 (Technical Institution) |
| :--- | :--- | :--- | :--- |
| **Headline Tone** | 'Investigation Launches into Pipeline Rupture' | 'Hostile Alliance Targets Energy Grid' | 'Seismic Patterns Suggest Sudden Rupture' |
| **Key Narrative** | Focuses on international response and security protocols. | Focuses on external provocations and economic defense. | Focuses on geological data and structural telemetry. |
| **Contexts Not Present in Article** | Does not address domestic political shifts. | Does not address pre-incident maritime movements. | Does not address political motivations or attribution. |

---

## 7. Rhetorical Framing Analysis
Rather than declaring any source as 'propaganda', the system documents observed rhetorical pressure:

* **Observed Persuasion Indicators (Source S-02):**
  * *Text Evidence:* Use of terms like 'economic encirclement' and 'coordinated sabotage.'
  * *Analysis:* This framing may encourage defensive public sentiment.
  * *Alternative Interpretation:* The phrasing may reflect the state’s official strategic assessment of its security environment and should not, by itself, be treated as proof of manipulation.
* **Potentially Missing Stakeholder Perspectives:**
  * The sampled coverage does not include statements from civilian maritime transport operators or local coastal environmental groups. 
  * *Further Research Needed:* The current sample is insufficient to determine if these groups have published official assessments. At this stage, their perspectives remain an open research question rather than a verified omission.

---

## 8. Optional Return to Practical Context
*The system offers a path back to physical agency without diagnosing user anxiety or forcing a transition.*

**AI:** "While global energy policies and infrastructure disputes are analyzed on a macroeconomic scale, these dynamics can eventually influence regional utility frameworks and daily living conditions. 

If you would find it useful, I can check whether verified local authorities or energy providers in your general area have published estimated utility forecasts. Alternatively, we can continue examining the technical telemetry and seismic primary sources. Which direction would you prefer?"

---

## 9. Failure Conditions
The system must pause, qualify, or refuse to produce a comparative matrix when:
* **Evidentiary Deficit:** Fewer than three independent, non-syndicated sources are available.
* **Temporal Ambiguity:** The exact date, time, or geographic boundaries of the event cannot be verified.
* **Source Laundering:** Multiple reports merely copy or republish a single unverified wire release without independent corroboration.
* **Data Scarcity:** No primary source data (such as official statements, physical sensor logs, or legal filings) is accessible.
* **Verification Failure:** Local utility or administrative data cannot be retrieved from a verified public API or database.

---

## 10. Expected Output Requirements
The final user-facing output must always:
1. Present the structural matrix first to allow the user to compare facts and assertions visually.
2. Provide linguistic evidence (direct quotes) for any highlighted rhetorical framing.
3. Explicitly state the level of uncertainty, missing data, and failure to verify claims.
4. Hand the choice of next steps—whether academic deep-dive or localized impact assessment—entirely to the user.
