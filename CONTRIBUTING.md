# Contributing

Small experiment, kept tidy.

## Rules that come first

- **No secrets and no private content** in the repository or in the shelf. A pin is readable by everyone who has access to the shelf. gitleaks scans staged changes before every commit.
- **The shelf link is written in the skill.** Do not add other links to private artifacts, files or accounts.
- **Claude deletes a pin only when asked.** Keep that rule in the skill.

## Commits

Use [Conventional Commits](https://www.conventionalcommits.org/): `type(scope): imperative summary`, 72 characters at most, no final period. The body explains why.

- Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`.
- Scopes: `skill`, `page`, `plugin`, `repo`.
- One logical change per commit.
- Credit AI pair programming with a `Co-Authored-By` trailer.

## Workflow

1. Branch from `main`: `feat/<topic>`, `fix/<topic>`, `docs/<topic>` or `chore/<topic>`.
2. Run `python3 scripts/check_repo.py`. CI runs the same check and a secret scan.
3. Try the change in a live Claude Code session. If you changed `page/shelf.html`, republish it as the artifact and check it at phone width.
4. Open a pull request, squash-merge, delete the branch. For a release, update `CHANGELOG.md`, bump the version in `.claude-plugin/plugin.json` (Claude Code only picks up a change when the version changes), and tag `vX.Y.Z`.

## One-time setup

```bash
brew install gitleaks pre-commit
pre-commit install
```
