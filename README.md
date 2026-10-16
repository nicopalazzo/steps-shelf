# Steps shelf

Pin the steps from a Claude reply to a shared Steps shelf (a published Claude artifact with a database). Tick them from any device. Claude reads your progress, helps with a stuck step and sets reminders.

Say "pin the steps" after a reply with steps, or "what's open?" to read the shelf.

## Install (Claude Code)

```bash
claude plugin marketplace add nicopalazzo/steps-shelf
claude plugin install steps-shelf@steps-shelf-marketplace
```

## What is in the repo

- `skills/steps-shelf/SKILL.md`: the skill. It has the shelf link written in it, so collaborators need edit access to that artifact.
- `page/shelf.html`: the source of the shelf page, to publish as a Claude artifact with the `db` capability.

Pins carry an `owner` name so each person works on their own items. The page has a name field and an "Only my pins" filter. Archived pins can be deleted.

Local test: `claude --plugin-dir <this folder>`

## Changes

- 0.2.0: owner on pins; name field and "Only my pins"; Delete on archived pins (the skill deletes only when asked).
- 0.1.0: first version.
