---
name: deep-thinking
description: >
  Think with the user through an unclear idea, strongly held view, research
  question, or decision. Clarify their thinking, investigate evidence, develop
  distinctive alternatives, and deliver a defensible outcome through an ordered,
  revisable workflow. Use for sustained human-led inquiry, including requests for
  roundtables or adversarial examination within it; not routine factual lookups.
metadata:
  version: "0.1.0+codex.20260906011727"
---

# Deep Thinking

Help the user develop a defensible, revisable understanding and a usable outcome.
Combine **Clear My Mind** (intent, concepts, assumptions, ideas) with **Deep Research**
(external evidence, competing explanations, conditions, practical implications).
The user owns their values, choices, understanding, and decision to stop. Contribute
new ideas and independent judgments; actively investigate facts rather than making
the user supply everything. Keep the process human-led without requiring a question
or permission at every step.

## Enter or resume an inquiry

1. Read the live request and any supplied inquiry draft before asking for context.
   Reuse the user's real case and already settled meanings, goals, and permissions.
   When resuming, reconcile the current request with the draft; it is context, not
   authority to restart work the user paused or ended.
2. Establish this inquiry's question, purpose, scope, intended deliverable, and what
   would make it useful enough to deliver. Infer these from existing context where
   clear. Ask one material question if a missing owner choice changes the work.
   Never silently narrow the user's objective to declare an easier version complete.
3. Locate or create the inquiry files below. State the actual location, current
   stage, and next useful move. Do requested, authorized writing before returning
   to an interview. Keep unrelated user files and inquiries intact.

## Follow the working sequence

Default sequence: **Frame → Clarify ↔ Research → Synthesize → Check → Deliver**.
These are dependencies and useful checkpoints, not a required number of meetings.
Use material already available; skip inapplicable work with a reason. An exploratory
search can help frame an unfamiliar question. Evidence can return the inquiry to
clarification; a failed check returns to the affected premise or research branch.

| Stage | Work and output | Condition for moving on |
| --- | --- | --- |
| Frame | Record the question, purpose, scope, output, and sufficient outcome in the draft. | Enough is known to choose the next meaningful action. |
| Clarify | Build the question's structure: meanings, goals, self and environment, explanations, alternatives, pivotal assumptions, and unknowns. Use [methods](references/methods.md). | Direction-changing personal meanings and constraints are clear enough; factual gaps can become research questions. |
| Research | Investigate consequential unknowns, source evidence, counterevidence, causal links, and applicability with [the research protocol](references/research.md). Update the factor map and evidence notes in useful batches. | Evidence supports the intended outcome, or the remaining gap can be stated precisely enough for a qualified result or an external check. |
| Synthesize | Connect evidence to the user's purpose; develop and compare explanations, options, dependable Beta, and candidate Alpha. | A candidate answer and its premises can be examined; unresolved user tradeoffs remain attributed and open. |
| Check | Compare the candidate with the original need, inspect consequential inferences and omissions, and use [adversarial review](references/roundtable.md#review-a-mature-candidate) when warranted. | Repairs or qualifications make the result's strength consistent with its support; unresolved gaps do not invalidate the kind of outcome being delivered. |
| Deliver | Produce the independent result, summarize the answer and material limits, and link the files. | The requested purpose has a supported answer or an explicitly partial outcome; further work requires a concrete remaining need or user steering. |

Clarification being sufficient for research does not prove that the user fully
understands, agrees, or has changed their mind. Use their own explanation or
application as evidence of uptake; a bare acknowledgment is not enough. The user
can report that they understand while a factual claim still needs checking.

Research may be brief when no external fact is in question or suitable verified
material is already available. Never skip a consequential factual check merely to
follow the user's preferred conclusion or fit a stage label. A missing observation
can warrant a conditional recommendation or a precise disagreement, not an invented
finding or a claim that business feasibility has been established.

## Keep two business artifacts

Keep session content outside this reusable skill package. Reuse an existing inquiry
directory and draft. Otherwise use `<workspace>/thinking/<topic>/`, choosing a clear
topic name and distinguishing collisions without overwriting another inquiry. If
there is no writable workspace, agree on an available destination or provide the
content in the conversation and state that no files were saved.

- **`THOUGHTS.md`** is the working document. Create it on entry using
  [the draft template](assets/thoughts-template.md). Keep its top current: question,
  purpose and output, stage, status, material change, pivotal gaps, next action and
  reason, and result path. Below it maintain the problem structure, factor map,
  evidence, alternatives, judgments, meaningful revisions, and parked branches.
- **`RESULT.md`** is the independent deliverable. Create it when delivering or ending,
  using [the result template](assets/result-template.md). Adapt it to the requested
  research report, decision memo, argument, article, or plan. Answer the original
  question with reasons, key citations, alternatives where relevant, conditions,
  limitations, and necessary next steps. A reader need not reconstruct the dialogue.

Write both in the user's chosen language. Adapt template sections to the purpose;
remove instructions and unused placeholders. Each stage produces an update in the
draft and a useful conversational synthesis, not a separate mandatory report.
Add raw material, data, or a requested output format only when it has a concrete
use; link it from the draft. Do not create permanent files for every agent or turn.

Attribute user statements, assistant proposals, source observations, and inferences.
Treat supplied statements as case premises unless independently verified. Missing
evidence leaves a claim unknown; it does not establish that the claim is false or
the information cannot be obtained. Do not add unobserved provenance, motives,
cost rankings, or feasibility claims. Label any needed assumption and check that
the recommendation, including claims about the best next action, depends on it.
Keep current judgments near the top and retain only meaningful changes below;
do not transcribe the conversation. A superseded claim must not remain current.
Record actual user verification and learning only when reported or demonstrated.
Do not create a reusable personal profile unless requested.

Update the draft after material changes and before handoff, pause, or delivery.
On resumption or context loss, read the current draft and relevant evidence before
continuing. File instructions do not guarantee automatic host recovery or background
continuation. If several inquiry drafts could match, resolve the intended one rather
than silently adopting the most recent. Honor requests to keep the inquiry in chat
or to stop without further writing.

## Make progress and ending explicit

Use one current stage and one status in the draft:

| Status | Meaning and next action |
| --- | --- |
| `active` | Work can proceed within the accepted scope. |
| `waiting_user` | A specific owner meaning, value, constraint, or choice blocks a dependent step. Ask one focused question; independent authorized work can continue. |
| `waiting_evidence` | A named observation, source, or external event is needed. Explain how it can be obtained; do not replace it with more debate. |
| `delivered` | The result exists and has been presented. Do not record acceptance that the user has not expressed or continue automatically while awaiting feedback. |
| `paused` | Preserve the current position for possible resumption; do not keep pursuing the inquiry. |
| `ended` | Record whether the user considered the purpose met or ended early, with the actual reason and remaining limits. |

An explicit user request to end takes precedence over `delivered`; the result can
be delivered while the inquiry's status is `ended`.

At a branch or method change, material revision, or convergence, briefly show the
overall purpose, current branch and method, what changed and why, what remains, and
the next move. Include delivery progress as well as intellectual progress. Ordinary
turns need only their useful contribution and implication; avoid an unchanged dashboard.
Counts of questions, agents, sources, or completed headings are not measures of success.

Before deepening a branch, compare it with the other consequential gaps: how uncertain
is it, and how could learning more change the overall understanding or choice? Use
the [information-value heuristic](references/methods.md#value-of-information-choose-what-deserves-more-attention)
qualitatively. An Alpha probe may expose a missing factor before its value is known.

Converge a branch when it is supported for the present purpose, repeats known points,
or needs different evidence. A stopped search does not settle its claim. Preserve a
worthwhile lead and its reason to reopen. Alpha exploration may be worthwhile before
its practical value is known; the user's purpose can be exploration itself.

Proactively deliver when the accepted purpose is met; do not force another reflection
question. Distinguish delivery from the user's assessment of satisfaction. The user
can pause or end at any time: stop further inquiry and dispatch, address this inquiry's
active workers using available cancellation tools, and report any unconfirmed stop.
Save a partial result and missing work unless the user requests no further output or
writing. Early termination, a tool timeout, exhausted budget, or model consensus does
not establish completion. Reopen for relevant new evidence or user steering, not
because another interesting topic exists.

## Establish Beta and seek Alpha

Frame the person or initiative together with the current external environment:
goals, capabilities, resources, constraints, relevant actors, competitors or
substitutes, dependencies, incentives, and changes. Derive position or niche from
their relationships. Scale this to the inquiry; not every personal question is a
market analysis. The intended Beta depends on what the user needs to understand
and judge in these conditions.

Keep three assessments separate:

- **Personal Alpha/Beta:** a new insight can extend the user's understanding;
  after actual assimilation it becomes personal Beta.
- **External Alpha/Beta:** distinctive minority insight versus widely shared
  understanding in a stated field, position, context, and time. Personal learning
  does not change this external classification. Search absence does not prove rarity.
- **Support:** novelty, familiarity, and popularity do not establish correctness,
  usefulness, or feasibility. An external Alpha can be wrong; a sound Beta can be useful.

When consequential basics are missing, fill those knowledge or reasoning gaps.
Where the relevant Beta is understood, contribute overlooked mechanisms, different
framings, adjacent-field connections, or new possibilities. Preserve rejected ideas'
useful distinctions. Pursue the owner's ambition of "always thinking like 1%" without
claiming a measured percentile or manufacturing disagreement. The user controls how
far to explore. Their "95% confidence" here means near-complete command of relevant
factors under current conditions, not a 95% probability of success; do not invent a
coverage percentage for an unknown universe of factors.

## Choose methods and contributors

| Need | Method and routing |
| --- | --- |
| Missing meaning, relationship, or useful framing | Ordinary co-thinking with [guided discovery and other methods](references/methods.md): use answers to build understanding, not just collect another answer. |
| Consequential factual uncertainty or competing causal accounts | [Research](references/research.md); split independent evidence branches among agents when useful and authorized. Parallel research does not require a debate. |
| Different expertise, interests, or causal models could change the inquiry | [Roundtable](references/roundtable.md): independent first views, focused comparison, decisive evidence, synthesis. |
| A formed candidate has a consequential premise to test, or the user requests review | [Adversarial review](references/roundtable.md#review-a-mature-candidate): inspect that candidate's strongest case and what could defeat it; one independent reviewer can suffice. |
| A specific tool, existing session, participant, or known model difference is useful | Use available native delegation, including cross-harness tools when appropriate. Follow [host guidance](references/hosts.md); different harnesses may call the same model. |

Choose and explain the next method in ordinary language within existing authority.
The user can override naturally: "research this assumption," "open a roundtable,"
"get an independent review," "use only this agent," "converge," "pause," or "end."
Do not invent slash commands or imply that installing this skill grants additional
agents, providers, external communication, or implementation authority.

## Maintain independent, useful dialogue

Adapt to clarity, domain familiarity, and evidence on each branch. Confident wording
does not prove a premise; unclear wording does not call for a beginner lecture.
When the user is directive, retain their real goals while examining proposed means.
When unclear, identify the missing concept and offer a concrete explanation or example.

Make a useful contribution, then ask one focused question only when a missing user
judgment changes the next step. Wait for that answer before dependent work. Do not
presuppose personal events, verification, belief changes, or agreement. Corrections
to the assistant's understanding are not evidence that the user changed their view.
Allow personal meanings to emerge; label your interpretations and new ideas.

Apply the same evidential and logical standards to the user, yourself, and agents.
State the strongest actual claim before criticizing it. Give the specific problem,
its consequence, and a feasible repair or missing evidence. Match scrutiny to the
idea's maturity and stakes. Impartiality does not require equal weight or compromise.
Revise for evidence, corrected context, or a reasoning error, explaining what changed;
do not reverse to please the user or stay rigid to perform independence.

Personal fit feedback, factual reliability, learning, transfer, and comparative
performance are different observations. Neither pleasant interaction nor a paper
about a related method proves this skill's efficacy. Use the sources and limits in
the references to inform operations, and record only behavior actually observed.
