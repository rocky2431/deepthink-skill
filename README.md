# Deep Thinking

[简体中文](README.zh-CN.md)

Deep Thinking is a human-led inquiry skill for Codex, Claude Code, native Kimi
Code, and zCode. It combines Clear My Mind and Deep Research: clarify the question,
investigate evidence, develop distinctive alternatives, examine a candidate, and
deliver a defensible result.

## Use

Invoke the installed main Skill and give it a real question, relevant context, and
the outcome you need. Existing context is reused; you do not have to complete a
fresh interview. Natural instructions can steer it: "research this assumption,"
"open a roundtable," "get an independent review," "use only this agent," "converge
into a decision memo," "pause," or "end."

The default sequence is **Frame → Clarify ↔ Research → Synthesize → Check → Deliver**.
Stages can use existing material and return to earlier work when evidence warrants.
The owner controls values, choices, and stopping. The assistant proactively delivers
when the accepted purpose is supported; delivery does not fabricate owner acceptance.

Each sustained inquiry uses two files in its existing directory, or by default in
`<workspace>/thinking/<topic>/`:

- `THOUGHTS.md`: current position, problem structure, factors, evidence, judgments,
  meaningful revisions, and unresolved branches.
- `RESULT.md`: an independently readable report, decision memo, argument, or plan,
  with key citations, conditions, limits, and any necessary next step.

An early stop produces an explicitly partial result unless the user asks for no
further writing. Stage updates do not create a report per stage or per agent.

## Native plugin installation

This repository follows the current Ultra-family plugin-only layout. The package
and its only Skill are both named `deep-thinking`. Install the plugin once per
host; do not also copy it into a user Skill directory or add forwarding commands.
Host-native invocation spelling can differ.

Clone the public repository, then use the resulting checkout with each host's
native plugin manager:

```sh
git clone https://github.com/rocky2431/deepthink-skill.git
cd deepthink-skill
DEEP_THINKING_REPO="$(pwd)"
```

No host, model, provider, or optional tool version is pinned. Use a host that
supports native plugins and Skills, with your own model and provider settings.
The commands below are examples; the installed host's help takes precedence.
The version in each plugin manifest identifies this plugin's release, not a
required host version. Catalogs resolve the package within the checkout without
pinning a release tag or commit.

### Codex

```sh
codex plugin marketplace add "$DEEP_THINKING_REPO"
codex plugin add deep-thinking@rocky-deep-thinking
codex plugin list --json
```

In a new session, invoke `$deep-thinking`. Codex uses the root
`.agents/plugins/marketplace.json` and the package's `.codex-plugin/plugin.json`.

### Claude Code

```sh
claude plugin validate "$DEEP_THINKING_REPO/plugins/deep-thinking" --json
claude plugin marketplace add "$DEEP_THINKING_REPO"
claude plugin install deep-thinking@rocky-deep-thinking
claude plugin list --json
```

In a new session, invoke `/deep-thinking:deep-thinking`. Claude discovers the
package's `skills/` through its native plugin layout. The repository includes a
`.claude-plugin/marketplace.json` catalog, also usable by zCode.

### Native Kimi Code

In the Kimi TUI, run `/plugins install` with the absolute local directory
`<repo>/plugins/deep-thinking`, then `/reload`. Invoke `/skill:deep-thinking`.
If the TUI treats quotes as literal path characters, paste the full path without
surrounding quotes, including when it contains spaces. These examples are TUI
commands; follow your installed Kimi's plugin help. The package uses
`kimi.plugin.json`; Kimi manages its installation location.

### zCode

Use zCode's native plugin marketplace to add this checkout, then find and install
Deep Thinking. Follow the installed application's UI if navigation labels differ.
Use the native `/skill` picker or `/skill deep-thinking`. The package includes
`.zcode-plugin/plugin.json`. The native CLI's `plugins list --json` and
`skills list --json` can verify discovery; the executable path depends on the
installation and need not be on `PATH`.

After changes, refresh and reinstall the package through the host's native plugin
manager, then use a new session. A source edit alone does not prove an installed
cache was refreshed. See [the dated validation record](RESULT.md) for previously
tested environments, observed behavior, and remaining limits. Those observations
are not installation requirements or guarantees for every host version.

## Where the methods live

| Location | Responsibility |
| --- | --- |
| [SKILL.md](plugins/deep-thinking/skills/deep-thinking/SKILL.md) | Entry, stages, state, artifacts, ending authority, Beta/Alpha, method routing, and independent dialogue |
| [methods.md](plugins/deep-thinking/skills/deep-thinking/references/methods.md) | Guided discovery, divergence/convergence, information value, and targeted intellectual standards |
| [research.md](plugins/deep-thinking/skills/deep-thinking/references/research.md) | Factors, primary evidence, contrary explanations, source-to-judgment reasoning, and evidence-driven revision |
| [roundtable.md](plugins/deep-thinking/skills/deep-thinking/references/roundtable.md) | Independent first views, focused cross-challenge, candidate review, evidence checks, and reasoned revision |
| [hosts.md](plugins/deep-thinking/skills/deep-thinking/references/hosts.md) | Native invocation, optional delegation, actual tool boundaries, and file-based resumption |
| [assets](plugins/deep-thinking/skills/deep-thinking/assets/) | Working-draft and independent-result templates |

References include the original sources and the limits of transferring their
findings into this workflow. Related studies motivate the design; they do not
establish that this Skill improves long-term reasoning, eliminates sycophancy,
or achieves a measured top percentile. Personal novelty, external distinctiveness,
and evidential support remain separate.

## Scope and validation

The plugin contains instructions and templates. It adds no background runner,
hooks, fixed debate quota, MCP server, provider subscription, or mandatory runtime
dependency. Research and delegation use capabilities the current host actually
provides and the owner has authorized. Missing capabilities are stated explicitly.

Run `python3 tests/check_package.py` for portable package checks. Native manifest
validation and actual host invocations are separate checks. The co-creation record
is in [THOUGHTS.md](THOUGHTS.md); it is not part of the installed plugin.
