# Deep Thinking

[English](README.md) · [简体中文](README.zh-CN.md)

Deep Thinking helps you work through unclear ideas, research questions and
decisions with an AI agent. It clarifies the question, investigates evidence,
compares possible answers and turns the work into a report, decision memo,
argument or plan.

It runs as a native plugin in Codex, Claude Code, Kimi Code or zCode. Clear My
Mind examines your intent, concepts and assumptions. Deep Research checks
external evidence and competing explanations. The two work together: a finding
can change the question, and a clearer question can change what needs research.

Use it for questions that need sustained discussion and investigation, such as
assessing a product direction or examining a strongly held view. Routine factual
questions can go directly to your agent.

Version: 0.2.1. The plugin contains a Skill, references and templates. Your host
provides the model and tools.

- [Install and start](#install-and-start)
- [Your first inquiry](#your-first-inquiry)
- [How an inquiry works](#how-an-inquiry-works)
- [Files and progress](#files-and-progress)
- [Current limits](#current-limits)
- [Documentation](#documentation)
- [Development](#development)

## Install and start

You need a host that can load native plugins and Skills. Deep Thinking uses your
existing model and provider settings; it does not pin host, model, provider or
optional tool versions. The version in the plugin manifests identifies the
plugin release.

Clone the repository and use the local checkout with your host's plugin manager:

```sh
git clone https://github.com/rocky2431/deepthink-skill.git
cd deepthink-skill
DEEP_THINKING_REPO="$(pwd)"
```

### Codex

```sh
codex plugin marketplace add "$DEEP_THINKING_REPO"
codex plugin add deep-thinking@rocky-deep-thinking
codex plugin list --json
```

Codex reads `.agents/plugins/marketplace.json` and the package's
`.codex-plugin/plugin.json`.

### Claude Code

```sh
claude plugin validate "$DEEP_THINKING_REPO/plugins/deep-thinking" --json
claude plugin marketplace add "$DEEP_THINKING_REPO"
claude plugin install deep-thinking@rocky-deep-thinking
claude plugin list --json
```

Claude Code uses `.claude-plugin/marketplace.json` and discovers the package's
`skills/` directory through its native plugin layout.

### Kimi Code

In the native Kimi Code TUI, run `/plugins install` with the absolute path to
`<repo>/plugins/deep-thinking`, then `/reload`. The package uses
`kimi.plugin.json`; Kimi manages its installation directory.

These are TUI commands. If Kimi treats quotes as path characters, paste the full
path without surrounding quotes, even when it contains spaces.

### zCode

Add the local checkout through zCode's native plugin marketplace, then find and
install Deep Thinking. The marketplace uses `.claude-plugin/marketplace.json`;
the package includes `.zcode-plugin/plugin.json`.

The native CLI's `plugins list --json` and `skills list --json` can check
discovery. Its executable path depends on the installation and may not be on
`PATH`.

### Native plugin entries

Reload plugins or start a new session after installation. Invoke the main Skill
through your host's entry:

| Host | Main Skill entry |
| --- | --- |
| Codex | `$deep-thinking` |
| Claude Code | `/deep-thinking:deep-thinking` |
| Kimi Code | `/skill:deep-thinking` |
| zCode | `/skill deep-thinking`, or select it in the Skill picker |

The plugin and its only Skill are both named `deep-thinking`. All four hosts
load the same Skill content. Install one copy per host to avoid duplicate
entries or an older user Skill taking precedence.

Installation syntax and UI labels can vary; follow your installed host's help
when they differ. The catalogs refer to the package inside the checkout without
pinning a release tag or commit. After updating the checkout, refresh and
reinstall through the native plugin manager, then start a new session. Editing
the source alone does not update an installed plugin cache.

## Your first inquiry

Open your agent in the workspace where you want to keep the inquiry. Invoke
Deep Thinking and describe the question, any relevant material and the result
you need. For example:

> Use Deep Thinking to assess whether this product direction is worth pursuing.
> Start with the needs and constraints in the project notes, investigate the
> assumptions that could change the decision, and produce a decision memo with
> alternatives and unresolved questions.

The agent reads the available context and establishes what the inquiry needs
to answer. It asks one focused question when a missing choice or personal
meaning changes the work. It investigates factual gaps with the available
tools and reuses background you have already provided.

You decide your values, tradeoffs and whether to continue. The agent contributes
ideas and independent judgments, explains its reasons, and revises them when
evidence or corrected context warrants a change.

## How an inquiry works

The default sequence is **Frame → Clarify ↔ Research → Synthesize → Check → Deliver**.

1. Frame the question, purpose, scope and intended result. Establish what would
   make that result useful enough to deliver.
2. Clarify meanings, goals, constraints and assumptions. Identify what is known
   and which gaps could change the direction.
3. Research those gaps. Inspect sources, contrary evidence and competing
   explanations, then connect the findings to the question.
4. Synthesize a candidate answer. Compare alternatives and state the premises
   each depends on.
5. Check the answer against the original need. Examine consequential inferences
   and omissions, then repair or qualify the result.
6. Deliver a document that stands on its own, with the answer, supporting
   evidence, conditions and remaining limits.

Existing material can satisfy a stage. New evidence can send the work back to
clarification or research. There is no fixed number of questions or rounds.
When a branch repeats known points or needs different evidence, the agent
records what remains and why it might be worth reopening.

Ordinary discussion is the default. Independent research branches can use
additional agents when useful and authorized. A roundtable compares perspectives
whose expertise or assumptions could change the answer. Adversarial review
examines a developed candidate for errors and omissions; one independent
reviewer may be enough. These methods use the contributors your host provides.

The Skill distinguishes personal learning from external novelty. An insight
that is new to you is personal Alpha; once understood and absorbed, it becomes
personal Beta. Whether it is unusual in a field is a separate question, as is
whether the evidence supports it. Familiar knowledge can be useful, and a novel
idea can be wrong.

You can steer the work in ordinary language: "research this assumption," "open
a roundtable," "get an independent review," "use only this agent," or "converge
into a decision memo."

## Files and progress

Each sustained inquiry reuses its existing directory. For new inquiries, follow
the requested location or the project’s existing `docs/` / `documents/` convention;
with no convention, `<workspace>/documents/<topic>/`. Existing `thinking/` inquiries
stay in place. The agent states the actual location at the
start and keeps the inquiry's material outside the reusable plugin package.

| File | Contents |
| --- | --- |
| `THOUGHTS.md` | Working draft: current stage and status, problem structure, evidence, alternatives, judgments, meaningful revisions and unresolved branches |
| `RESULT.md` | Deliverable: report, decision memo, argument or plan, with key citations, conditions, limits and any necessary next step |

The agent creates the draft when the inquiry starts and writes the result when
delivering or ending. Both use your chosen language. Stage updates go into the
draft; separate reports for each stage or contributor are unnecessary.

Progress updates explain what is settled and why, what remains open and the next useful action.
The agent delivers when the agreed purpose has a supported answer. Delivery
records that a result is ready; your acceptance remains yours to give.

You can say "pause" or "end" at any time. An early stop leaves a partial result
with the unfinished work stated, unless you ask for no further writing. You can
also keep an inquiry in chat without saving files. To resume saved work, ask the
agent to read the inquiry's `THOUGHTS.md` and continue from the current position.

## Current limits

Research and delegation depend on the tools and permissions available in the
host. The plugin adds no background runner, hooks, MCP server, provider
subscription or mandatory runtime dependency. Saving a draft supports resumption;
it does not provide automatic recovery after context compaction or background
continuation.

The model remains responsible for following the workflow. Outputs can contain
unsupported inferences or incorrect progress labels. Agreement among agents,
a reputable source or a completed document does not establish that a conclusion
is correct.

The references explain the research behind the methods and the limits of
applying it here. That research does not establish this Skill's effectiveness.
Stable reasoning quality across problems, long-term learning, reduced sycophancy
and an advantage over ordinary conversation remain unproven.

## Documentation

- [Skill instructions](plugins/deep-thinking/skills/deep-thinking/SKILL.md):
  workflow, states, stopping, artifacts and method selection.
- [Clarification methods](plugins/deep-thinking/skills/deep-thinking/references/methods.md):
  guided discovery, exploration and convergence, information value and reasoning checks.
- [Research protocol](plugins/deep-thinking/skills/deep-thinking/references/research.md):
  source evidence, competing explanations and revisions to the question.
- [Roundtables and review](plugins/deep-thinking/skills/deep-thinking/references/roundtable.md):
  independent initial views, focused challenges and review of a candidate answer.
- [Host guidance](plugins/deep-thinking/skills/deep-thinking/references/hosts.md):
  native entries, available tools, delegation and resumption.
- [Templates](plugins/deep-thinking/skills/deep-thinking/assets/): working draft
  and independent result.

## Development

The package check uses the Python standard library. Run it from the repository
root:

```sh
python3 tests/check_package.py
```

It checks the four manifests, version consistency, the single Skill entry,
marketplace catalogs, templates and local links. Native plugin loading and the
quality of an actual inquiry require separate checks in the host.
