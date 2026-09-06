# Host Execution and Recovery

Use this reference when invoking the skill, choosing delegated work, resuming an
inquiry, or stopping its active workers. Discover the current host's capabilities.

## One plugin, one main skill

The plugin and main skill are both named `deep-thinking`. Clarification, research,
and roundtables are parts of this skill; they do not need separate aliases.

| Host | Native explicit entry |
| --- | --- |
| Codex | `$deep-thinking` |
| Claude Code | `/deep-thinking:deep-thinking` |
| Kimi Code | `/skill:deep-thinking` |
| zCode | `/skill deep-thinking`, or select it in the Skill picker |

Confirm discovery in the actual host. Resolve references and templates from the
loaded skill directory, not from the inquiry's working directory or a guessed
cache path. Follow the installed host's help when its command syntax differs.
Do not assume a particular executable path or manually edit installed caches.
Installation procedures belong in the package README.

This skill does not pin host, model, provider, or optional tool versions. Use the
host's configured model and provider unless the user requests a different choice.
Select tools by their available capabilities and current contracts.

## Select available capabilities

Inspect the host's native research tools and available agents before choosing a
route. Select contributors for relevant expertise, context, tools, or independent
perspectives. A different harness may use the same model. Pass the original
question, necessary material, scope, allowed effects, and expected result; workers
do not automatically inherit the caller's conversation or model choice.

Use native delegation when it fits. For cross-host work through an available
`agent-delegation` skill, read its installed instructions and follow the current
bridge contract. Listing a target proves capability, not additional authorization.
Carry the owner's existing authority without expanding it or asking for it again.
Use caller and chain metadata only from known provenance; it is not permission.

If a required tool or agent is unavailable, state the limitation and use an adequate
available method. Label simulated perspectives as simulated. If independent work
or external evidence is required, keep that requirement unresolved rather than
claiming an equivalent result. Do not install providers or runtimes implicitly.

## Submit, observe, and continue

These are native bridge commands; use the installed skill and CLI help if they differ:

```sh
agent-delegate list --json
agent-delegate submit --to <target> --cwd <absolute-inquiry-root> --task "<mission>"
agent-delegate wait --id <delegation_id> --timeout 30
```

Submit once and retain the full returned ID with its branch in `THOUGHTS.md`, or in
the conversation when files are not being maintained. Use `--task-file` for a longer
mission when useful. A successful command exit does not establish task success.
Read each result: `terminal: false` or `wait_timed_out: true` means observe the same
ID again; an observation timeout is not cancellation and must not trigger resubmission.
`status --id <delegation_id>` retrieves immediate progress or the completed result.
If the submit response is lost, recover its ID from the receipt before retrying.

Omit `--session` for independent tasks, including several tasks sent to one target.
For an intentional conversational follow-up, submit with the same target, cwd, and
session name used on the first task. There is no separate `resume` bridge command:
resume observation with the task ID, or continue conversation with that named session.
Inspect partial output, native state, and possible effects before retrying an
`incomplete` or `execution_state: unknown` result. Wrapper termination does not prove
the worker stopped. Integrate returned reasoning and verify consequential evidence.

## Recover and stop

After context loss or handoff, read the intended inquiry's current `THOUGHTS.md`,
relevant evidence, result path, and retained worker IDs. Reconcile them with the live
request. A saved task does not authorize restarting a paused or ended inquiry.
This skill provides file-based recovery instructions; it does not supply hooks,
guarantee automatic compaction recovery, or schedule background continuation.

When the user stops the inquiry, stop dispatching and use actual cancellation tools
for its active workers. With the bridge, call `agent-delegate cancel --id <delegation_id>`,
then inspect that ID with `status` or `wait`. Acknowledgment is not proof of stopping;
report an unresolved outcome honestly. A native cancelled turn may leave spawned
commands running: inspect and stop this task's jobs through available native controls
when required, without disturbing other tasks. Preserve the partial result and limits
under the main skill's ending rules; honor requests for no further output or writing.
