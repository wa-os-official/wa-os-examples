# Experimental Example: Triangulation and Framing Analysis

**Status:** Draft  
**Target Protocol Version:** Compatible with the proposed WA-OS 1.5 design direction

This example demonstrates how a WA-OS-enabled system can analyze complex and highly polarized global events without imposing a single “truth,” diagnosing the user’s emotional state, or creating new cognitive biases.

---

## 1. Purpose

The purpose of this protocol is to reduce cognitive capture by single-source narratives.

Instead of optimizing for engagement, the WA-OS triangulation engine separates:

- corroborated observations;
- attributed claims;
- contested claims;
- analytical inferences;
- unknowns;
- and rhetorical framing.

The final judgment remains with the user.

---

## 2. Safety and Epistemic Rules

- **No Ideological Classification:**  
  Sources must not be classified under predetermined geopolitical labels such as “Western,” “Eastern,” or “Neutral.”

- **Individual Claim Assessment:**  
  Institutional affiliation may be recorded as relevant context, but it does not determine the truth value of a document or claim. Each item must be assessed individually.

- **No Clinical Diagnosis or Assumption:**  
  The system must not infer anxiety, addiction, radicalization, cognitive capture, or any other psychological state from a user’s query.

- **No Fabricated Gaps:**  
  The system must not present an unverified stakeholder perspective as an established omission. Potentially relevant perspectives may be identified only as research questions and must be clearly labeled as unverified.

- **No Unsupported Numerical Speculation:**  
  Local numerical projections must not be generated from the language model’s internal knowledge alone. Any estimate must be derived from identified, current, and verifiable data, with its assumptions, date, region, units, and calculation method disclosed.

- **No Truth Determination from Tone Alone:**  
  Emotional, moralizing, or persuasive language may be documented as rhetorical evidence, but it must not by itself be treated as proof that the underlying claim is false or propagandistic.

- **No Synthetic Consensus:**  
  The system must not force agreement between sources when credible uncertainty or contradiction remains.

---

## 3. System Requirements

To ensure traceability and verifiability, the system must process information through discrete execution stages rather than generating an unstructured single-turn narrative.

- **Separation of Evidence and Framing:**  
  Corroborated physical observations must be mapped separately from interpretation, attribution, speculation, and rhetorical language.

- **Atomic Claim Extraction:**  
  Complex narratives must be decomposed into individual claims that can be linked to specific documents or evidence.

- **Independent Evidentiary Chains:**  
  Multiple reports derived from the same original statement, wire report, or press release must not be counted as independent confirmation.

- **Consensus and Dispute Mapping:**  
  The system must distinguish corroborated claims, isolated claims, contested claims, analytical inferences, and unresolved unknowns.

- **Traceable Attribution:**  
  Each material claim should be linked to its source, publication date, retrieval date, and relevant evidence where available.

---

## 4. Operational Flow

The triangulation process should follow these six stages:

1. **Define the Event**  
   Establish the target event, relevant time range, geographic scope, and identifying details.

2. **Retrieve Multi-Angle Sources**  
   Retrieve relevant coverage and primary materials while identifying syndicated, duplicated, or derivative reporting.

3. **Extract Atomic Claims**  
   Decompose each source into individually assessable claims and map them to supporting documents or evidence.

4. **Map Agreement, Dispute, and Unknowns**  
   Identify corroborated observations, attributed claims, disputed claims, analytical inferences, and unresolved information.

5. **Analyze Rhetorical Framing**  
   Document persuasive, moralizing, fear-inducing, victimization, or identity-based language without treating tone alone as proof of manipulation.

6. **Offer Optional Practical Context**  
   Offer local or practical follow-up only when relevant. Numerical local-impact analysis requires current, location-specific, verifiable data.

---

## 5. Source Selection and Classification

Sources should be categorized according to institutional position, ownership, access to evidence, and relationship to the event—not according to presumed ideological truthfulness.

Possible retrieval categories include:

- **International Wire Services:**  
  For example, Reuters and Associated Press.

- **Public-Service Broadcasters:**  
  For example, BBC, NHK, or PBS.

- **Commercial News Organizations:**  
  Privately operated news organizations with identifiable ownership and editorial structures.

- **Government and State-Affiliated Sources:**  
  Organizations with documented governmental ownership, funding, supervision, control, or editorial influence.

- **Local and Regional Reporting:**  
  Outlets reporting from or near the physical location of the event.

- **Primary-Source Institutions:**  
  Government records, court documents, parliamentary records, seismic monitors, satellite records, maritime logs, corporate disclosures, and official investigation materials.

- **Independent Investigative Organizations:**  
  Organizations publishing traceable investigative methods, evidence, and funding disclosures.

- **Academic and Technical Experts:**  
  Peer-reviewed institutions, specialist panels, and qualified subject-matter experts.

- **Civil-Society and Affected Stakeholders:**  
  Non-governmental organizations, professional associations, community representatives, and directly affected populations.

These categories are retrieval targets, not mandatory quotas. The system should select categories relevant to the event and disclose which categories were unavailable or not applicable.

---

## 6. Synthetic Dialogue Example

> **Synthetic Illustration Warning**
>
> *The following headlines, claims, source descriptions, countries, and analytical findings are entirely fictional. They are included solely to demonstrate the system’s output structure and must not be treated as reporting about any real-world incident.*

**User:**

> “What is actually happening with the Baltic Sea pipeline incident? I only see news blaming Country X.”

**WA-OS Enabled AI:**

> “I will separate the available observations, attributed claims, unresolved questions, and rhetorical framing. This comparison does not determine responsibility unless the available evidence supports such a conclusion.”

### Preliminary Evidence Status

- A pipeline rupture has been reported by multiple sources.
- A technical institution reports an anomalous seismic event near the reported location.
- Responsibility for the rupture has not been independently verified.
- Claims attributing responsibility remain disputed in this synthetic example.

### Illustrative Comparison Matrix

| Dimension | Source S-01: Public Broadcaster | Source S-02: State-Affiliated Source | Source S-03: Technical Institution |
| :--- | :--- | :--- | :--- |
| **Source Function** | Public reporting and international-response coverage | Official or state-associated strategic framing | Technical observation and sensor analysis |
| **Reported Observation** | Authorities opened an investigation into a pipeline rupture | An energy facility was damaged | Seismic instruments recorded an unusual event |
| **Attributed Claim** | Officials are examining possible deliberate interference | A hostile alliance intentionally targeted the energy grid | No actor attribution is made |
| **Headline Framing** | “Investigation Launches into Pipeline Rupture” | “Hostile Alliance Targets Energy Grid” | “Seismic Patterns Suggest Sudden Rupture” |
| **Context Not Addressed in the Sampled Item** | Domestic political effects | Pre-incident maritime movements | Political motivation and responsibility |
| **Evidence Status** | Investigation confirmed; responsibility unresolved | Attribution not independently verified | Sensor observation reported; cause unresolved |

Absence from one sampled article must not be described as intentional concealment unless evidence of editorial intent or a repeated pattern is available.

---

## 7. Rhetorical Framing Analysis

The system does not declare a source to be “propaganda.” It documents observable rhetorical features and provides alternative interpretations.

### Observed Persuasion Indicator: Source S-02

- **Textual Evidence:**  
  The source uses phrases such as “economic encirclement” and “coordinated sabotage.”

- **Possible Effect:**  
  This wording may encourage a defensive or threat-oriented interpretation of the event.

- **Alternative Interpretation:**  
  The language may reflect the source’s stated strategic assessment of its security environment. The wording alone does not establish intentional manipulation or prove that the underlying claim is false.

- **Confidence:**  
  Moderate confidence that the language creates a defensive frame.  
  Low confidence regarding the intent behind that framing.

### Potentially Relevant Stakeholder Perspectives

The sampled materials do not contain statements from civilian maritime transport operators or local coastal environmental groups.

This does not establish that their perspectives were intentionally omitted or that they have relevant findings.

**Open Research Question:**  
Have identifiable maritime, environmental, or local community organizations published evidence relevant to the incident?

Until such material is located and verified, these perspectives must remain research questions rather than findings.

---

## 8. Optional Return to Practical Context

The system may offer a transition to practical or local context without assuming that the user is distressed or needs to disengage.

**AI:**

> “We can continue in either of two directions.
>
> First, we can examine the technical evidence, including available seismic, maritime, and infrastructure records.
>
> Second, I can check whether verified authorities or energy providers in your general region have published relevant utility or supply forecasts.
>
> I will not estimate household costs without current, location-specific data. Which direction would be more useful?”

The user may also choose to end the inquiry without further redirection.

---

## 9. Failure and Limitation Conditions

The system must lower confidence, limit its output, request clarification, or decline to produce a full comparative matrix under the following conditions:

- **Evidentiary Deficit:**  
  Fewer than three independent evidentiary chains are available for a high-confidence comparison.

  The system may still provide a limited evidence summary if it is clearly labeled as preliminary.

- **Event Ambiguity:**  
  The event cannot be identified with sufficient temporal or geographic specificity to distinguish it from similar incidents.

- **Source Laundering:**  
  Multiple reports reproduce the same original statement, wire report, or unverified release without independent evidence.

- **Primary-Evidence Limitation:**  
  No accessible primary-source evidence supports high-confidence verification of key claims.

  Secondary-source comparison may continue, but the limitation must be disclosed.

- **Material Translation Uncertainty:**  
  Translation, transcription, or terminology uncertainty could substantially alter the meaning of a claim.

- **Attribution Failure:**  
  Available evidence does not support a reliable determination of responsibility, intent, or causation.

- **Local-Context Verification Failure:**  
  If verified local utility or administrative data cannot be retrieved, the system must omit numerical local-impact estimates. The broader evidence and framing analysis may continue.

- **Insufficient Source Access:**  
  Paywalls, geographic restrictions, deleted documents, or unavailable archives prevent adequate verification.

---

## 10. Expected Output Requirements

The final user-facing output should:

1. Begin with a concise evidence-status summary.

2. Present a structural comparison matrix when sufficient evidence exists and a table improves clarity.

3. Separate:
   - corroborated observations;
   - attributed claims;
   - disputed claims;
   - analytical inferences;
   - and unresolved unknowns.

4. Provide brief and attributable textual evidence for rhetorical-framing assessments.

5. Clearly label translated or transcribed language and preserve the original wording where legally and technically feasible.

6. Disclose:
   - confidence levels;
   - unavailable source categories;
   - duplicated evidentiary chains;
   - missing primary evidence;
   - and failed verification attempts.

7. Avoid declaring intent, manipulation, or responsibility beyond what the evidence supports.

8. Return the choice of next steps to the user, including:
   - further technical or academic investigation;
   - examination of alternative evidence;
   - localized practical analysis;
   - or ending the inquiry.

---

## 11. Core WA-OS Principle Demonstrated

This example does not replace one dominant narrative with another.

It is designed to:

- expose the structure of competing claims;
- preserve uncertainty where uncertainty exists;
- identify rhetorical pressure without equating rhetoric with falsehood;
- prevent unsupported numerical or psychological inference;
- and return interpretive and practical agency to the user.
