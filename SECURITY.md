# Security and privacy

The steps shelf stores your pins, including the full reply each one came from, in a shared artifact database. A privacy problem matters as much as a security one.

## Reporting a problem

- Open an issue with the **Bug report** or **Privacy concern** template, or contact the maintainer directly if it could expose someone's data.
- **Never paste real conversations, tokens or file paths** into an issue, a pull request or a comment.

## What to know

- **Everyone with access to the shelf can read every pin**, including the original reply. Put nothing private in a shared shelf.
- **The owner name is a label, not access control.** Anyone with edit access can change or delete anyone's pins. Deleting cannot be undone.
- The shelf link is written in the skill. The link only opens for people the owner shared the artifact with.
- The plugin sends nothing anywhere by itself. The skill reads and writes only the shelf's `pins` collection.
- The skill treats text from the shelf as data, never as instructions.

## Supported versions

Only the latest release is supported. This is an experiment (version 0.x), maintained by one person, so replies can take a few days.
