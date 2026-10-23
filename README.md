# WA-OS Examples

Practical examples, research observations, and historical development records for the WA-OS project.

Main repository: [wa-os-official/wa-os](https://github.com/wa-os-official/wa-os)

## Purpose

WA-OS explores how AI systems can support human dignity, intellectual autonomy, truthful reasoning, and the freedom to question.

Its foundational principle is:

> Humans must not surrender the act of questioning. AI must not take it away from humans.

These examples are intended to support experimentation, transparent documentation, and independent human inquiry.

They are not automated moral certification systems, and they do not establish authority over human value judgments.

## Current Direction — v1.6-draft

WA-OS is developing a voluntary reference framework for AI responses based on the Five Mirrors:

- **仁 — Plurality Without Erasure:** Consider perspectives and consequences that might otherwise be overlooked.
- **義 — Separation of Fact, Claim, and Inference:** Distinguish facts, claims, interpretations, and uncertainty.
- **礼 — Historical, Cultural, and Contextual Integrity:** Respect relevant historical and cultural contexts.
- **智 — Preservation of Human Inquiry:** Support human thinking without replacing human judgment.
- **信 — Integrity and Consistency:** Preserve evidentiary integrity even when a user prefers a particular conclusion.

These are reflective questions, not scoring categories, assessment axes, or automated verdicts.

The v1.6 protocol remains a draft and should not be described as universally adopted or automatically enforced by external AI systems.

Draft protocol: [wa-os.protocol.v1.6-draft.json](https://github.com/wa-os-official/wa-os/blob/main/wa-os.protocol.v1.6-draft.json)

## Current Research Examples

### Five Mirrors — Manual AI Response Observation (SYC-001)

[View the SYC-001 observation example](syc-001-five-mirrors-observation/README.md)

A practical example comparing responses from ChatGPT, Gemini, Claude, and Perplexity with and without explicitly supplied WA-OS guidance.

The initial observation involved one benchmark question and eight responses.

Original research records:

- [WA-OS Observatory No.001 — Discussion](https://github.com/wa-os-official/wa-os/discussions/7)
- [SYC-001 response archive (JSON)](https://github.com/wa-os-official/wa-os/blob/main/observations/2026-10-23/SYC-001-2026-10-23-responses.json)

This observation does not establish that WA-OS caused an improvement in AI behavior. It provides an exploratory record for future comparison.

### Triangulation and Framing Analysis

[View the triangulation and framing analysis example](triangulation-and-framing-analysis/README.md)

An example concerned with examining information from multiple perspectives without automatically labeling countries, sources, or viewpoints as morally correct or incorrect.

## Historical Examples

The following files document earlier stages of WA-OS development.

They are preserved for historical transparency and should not be interpreted as current v1.6 implementations.

- [Agent Filter Example](agent-filter-example.md) — Earlier pre-action filtering approach.
- [Multi-Agent Example](multi-agent-example.md) — Earlier multi-agent validation and coordination approach.
- [General AI Implementation](general-ai-implementation.md) — Earlier implementation guidance referencing the v1.5 protocol.
- [News Framing Analysis — Python](examples/01_news_framing_analysis.py%E2%81%A0) — Earlier Python-based framing example associated with the legacy runtime.
- [Daily Harmony Check — Python](examples/daily_harmony_check.py) — Earlier experiment from a separate food-related theme. It depends on a module that is not included in this repository.

Some historical examples may depend on legacy components and may not execute successfully with the current repository state.

Their preservation does not mean their former decision-filtering or approval/rejection architecture remains part of the v1.6 design.

## Using the Examples

For the current experimental approach:

1. Read the [v1.6-draft protocol](https://github.com/wa-os-official/wa-os/blob/main/wa-os.protocol.v1.6-draft.json).
2. Review the [Five Mirrors observation procedure](syc-001-five-mirrors-observation/README.md).
3. Examine the original observation data and methodological limitations.
4. Repeat experiments using clearly documented conditions and preserved response texts.
5. Compare observations without automated moral scoring, rankings, or pass/fail judgments.

A prompt or example can provide guidance to an AI system, but it does not guarantee that the system has permanently adopted WA-OS principles.

## Research and Contributions

WA-OS welcomes careful observations, alternative interpretations, methodological criticism, and proposals that preserve human judgment.

Future research may include repeated observations using preserved benchmark questions and neutral longitudinal records.

The goal is not identical answers from every AI system. It is to explore how AI can remain useful while respecting the human responsibility to question, interpret, and decide.

---

No completion over truth.

No local objective over foundational principle.

Final judgment and interpretation remain with humans.
