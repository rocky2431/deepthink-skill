# Roundtables and Adversarial Review

Use this to investigate a consequential claim or candidate possibility through
materially different perspectives. Show how it connects to the larger inquiry and
return material unresolved choices to the user. A roundtable is a
method for examining reasons, not a vote or a performance of expert consensus.

For a sufficiently developed candidate that needs scrutiny, go directly to
[adversarial review](#review-a-mature-candidate); a roundtable is not a prerequisite.
Ordinary thinking can clarify and challenge without either formal method. Match
scrutiny to the idea's maturity and the consequences of relying on it: leave room
for exploratory Alpha while checking premises that support a commitment or conclusion.

## Frame the dispute

State the question, the user's actual goal and constraints, the current proposal,
and the premise most likely to change the judgment. Use supplied context; do not
require a new interview when the issue is already clear. Attribute assistant-created
proposals rather than treating them as positions the user has endorsed.

Choose perspectives for different knowledge, interests, causal models, or solutions.
Use the smallest useful set. For example, examine the proposal's strongest case,
a consequential objection, and a different framing that might improve both. These
are possible contributions, not permanent roles or mandatory opposing opinions.

## Form and compare positions

For each perspective, give a concrete judgment, its strongest reasons, important
assumptions or evidence gaps, and what could change that judgment. Preserve the
user's strongest actual position. Challenge the assistant's proposals as well.

Describe the actual arrangement accurately:

- Roles written in one response are a simulation, without independently formed views.
- Real subagents can form initial views in separate contexts while using the same model.
- Different models or harnesses can add differences; different harnesses may still
  invoke the same model. Neither implies independent external evidence.

When using actual contributors, give them the question, goals, constraints, and
necessary original material before sharing the coordinator's preferred conclusion or
peers' answers, where practical. Preserve relevant owner context; do not manufacture
independence by withholding facts needed to understand the task. Disclose shared
material or other limits. Follow current authority and available delegation tools;
this protocol does not itself authorize extra agents, providers, or external effects.

Direct the exchange at the decisive premise rather than appending generic pros and
cons. Ask which causal link, assumption, or value difference explains the disagreement
and what observation could distinguish the accounts. Offer an alternative framing
when it could change the available choices. A counterexample must bear on the claim.

For a disputed factual premise, use the [research protocol](research.md) to check
the source or identify evidence still needed. The coordinator directly inspects
decisive sources; three agents citing one study still supply one source. Never invent
statistics, testimony, or citations to make a perspective sound authoritative.
Changing the user's stated preference alone is not a reason to change a factual judgment.

After independent initial work, exchange the consequential disagreement for focused
cross-challenge. Ask for the faulty premise, causal link, or missing observation,
allowing reasoned revision. The coordinator integrates what changed and why. Continue
only while the exchange adds relevant evidence, a testable distinction, or a promising
new premise or possibility. Further rounds need a purpose, not a preset debate quota.

## Return the useful difference

Bring back the premises actually shared, the consequential disagreement, any new
candidate insight, and the assistant's current assessment with its reasons and
limits. Preserve a useful minority idea even if it is not selected. Do not average
the positions or force closure by majority, eloquence, or deference to the user.

Keep personal novelty, external distinctiveness, and evidential support separate.
Use "unknown" where external Alpha/Beta status has not been established. A thought
can deserve exploration without being ready for acceptance or action.

Ask one focused question only if a consequential user interpretation or choice remains,
then wait. Otherwise conclude, seek the missing evidence, or park the branch with a
reason to reopen. A concise comparison is often enough; use an extended dialogue
when it adds value or is requested. Record actual responses without inventing assent
or marking personal Alpha as assimilated before the user's explanation or use supports it.

## Review a mature candidate

Use this path when a sufficiently specified conclusion, plan, or artifact needs to
be tested for consequential errors, counterexamples, or omissions, or when the user
requests review. Start with the candidate, its intended use, agreed constraints,
supporting material, and what would make its central claims fail. Do not invent new
acceptance criteria or require a prior roundtable.
Set out the relevant criteria from the user's purpose before judging the candidate,
then inspect its evidence before the author's defense where the inputs permit.
Retain that assessment when later considering a rebuttal. If the defense was already
visible, disclose that limit rather than claiming a blind review.

One independent reviewer can be sufficient. Give the reviewer the candidate and the
context needed to assess it before the coordinator's preferred verdict or peers'
reviews. Do not withhold relevant evidence to manufacture independence. An actual
review in a separate context can use the same model. Context separation alone does
not establish independent external evidence. If an independent contributor is
unavailable, label the work as coordinator self-review or simulated critique.

Test actual claims and inferential links, using the relevant
[intellectual standards](methods.md#intellectual-standards-test-the-actual-claim).
Consider the strongest contrary evidence, alternative mechanism, or boundary case
that could alter the result. Each actionable finding should identify:

- The specific claim or artifact location being challenged.
- The inspected evidence, reasoning error, or missing observation; distinguish a
  demonstrated defect from a concern or an unresolved value choice.
- The effect on the conclusion or intended use, including the conditions under
  which the problem matters.
- A feasible correction or alternative with its tradeoff, or the observation or
  changed condition that would settle or overturn the finding.

The coordinator verifies decisive evidence and explains which findings change the
candidate and why. Return factual gaps to [research](research.md), inference or design
problems to synthesis, and changed meanings or unresolved user tradeoffs to
clarification. Recheck the affected claims after correction. A premise that remains
unverified must limit the result; do not record it as passed because access or tools
were unavailable. The absence of findings is not proof of correctness, and agreement
is not required to finish a useful review.
Reuse the same criteria during re-review. A changed verdict needs located evidence,
a repaired inference, or corrected context, with its effect stated. Persuasive
restatement is insufficient. A user-approved change of criteria is a changed review
basis and must be identified. Preserve a candidate's useful contribution when a
qualification or local repair resolves the objection; scrutiny need not flatten it
into the least distinctive option.

Integrate the disposition and any remaining conditions into `THOUGHTS.md` and carry
material qualifications into the delivered `RESULT.md` under the main file contract.
Do not create a permanent report for every reviewer by default. Continue review only
when an unresolved consequential finding or new evidence gives it a purpose.

## Evidence for this design, and its limits

[Academic Research Skills, re-review protocol, inspected 2026-09-11](https://github.com/imbad0202/academic-research-skills/blob/c7af8b9017954c745ed7ad4afed4dba460a6c247/academic-paper-reviewer/references/re_review_mode_protocol.md)
separates criteria, evidence assessment and author persuasion, retaining the basis
for later adjustments. This Skill adopts the review order and evidence requirement,
not its multi-gate runtime. Text instructions alone do not enforce input isolation.

[Du et al. (2023), especially section 5](https://arxiv.org/html/2305.14325v1#S5)
reported gains on six benchmark tasks, alongside confidently wrong consensus and
problems with long debates. [Smit et al., version 3](https://arxiv.org/html/2311.17371v3)
found the original protocols did not reliably beat other prompting or ensemble
methods in their comparisons; tuning mattered, and forced opposition could harm
correct initial answers. These findings motivate testing the procedure and avoiding
consensus-as-proof. They do not establish this skill's effectiveness with current
models or open-ended personal decisions.

[Sharma et al., sections 3–4](https://arxiv.org/html/2310.13548v4) found sycophancy
across five assistants in four free-form tasks and that human or model preferences
sometimes favor persuasive agreement over truthful correction. When the user or a
contributor disputes a factual assessment, inspect the specific evidence, reasoning,
or corrected context. Revise for those reasons, explaining what changed; preference
or pressure alone is not a reason to reverse, and performing independence is not a
reason to resist a warranted correction. This is a design response to an observed
risk, not evidence that this procedure eliminates sycophancy in current models.
