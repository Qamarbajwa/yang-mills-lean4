# READ-ONLY Gemini CLI hook example — NOT production enforcement

Files here are **examples**, not automatically installed into a target project. Gemini should first inspect the existing `.gemini/settings.json` and `GEMINI.md`, validate the installed CLI version and actual hook schemas, and create an isolated candidate branch. A safe proposed integration is `settings.READ_ONLY.example.json` merged under `.gemini/settings.json` with the hook copied to `.gemini/hooks/deny_mutations.py` and the relevant project context merged into `GEMINI.md`.

Test actual hook behavior: read_file allowed, `write_file`, `replace`, `run_shell_command`, `mcp_*`, `apply_patch` and all unfamiliar tools denied. Read-only access must still be restricted by OS/repository permissions so secrets are not exposed. Tool hooks can be disabled, modified, or misconfigured by a sufficiently privileged agent; **do not claim they enforce permissions independently**. The documented malformed-hook failure path may default to allow, so test exit code 2 on malformed inputs and set OS ACLs for real safety.

There is no automatic switch here into autonomous write mode. The trusted external host, policy gateway and owner must separately grant a scoped writer token using independent credentials; workers should never possess that host's administration secrets.
