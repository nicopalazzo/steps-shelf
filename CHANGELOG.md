# Changelog

All notable changes to steps-shelf. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Screenshots of the shelf page (sample data) in the README.
- Repository standards: licence, contributing guide, security note, issue and PR templates, a `check` workflow and a secret scan.

## [0.3.1] - 2026-10-16

### Changed

- The spoken command is now "add to the shelf" instead of "pin the steps", because another tool uses "pin". The skill ignores the word "pin". Stored data (the `pins` collection and `p-` ids) is unchanged, so existing shelves keep working.

## [0.3.0] - 2026-10-16

### Changed

- Each user gets their own shelf. The skill reads the shelf link from `~/.claude/steps-shelf-url` and, when the file is missing, offers once to publish the shelf page as the user's own private artifact.
- The repo no longer contains any shelf link. A check fails if one is added.

## [0.2.2] - 2026-10-16

### Changed

- The skill opens the shelf in the side pane every time it reads the shelf, not only after a pin.

## [0.2.1] - 2026-10-16

### Added

- The skill opens the shelf in the side pane after every pin, so the user sees the result at once.

## [0.2.0] - 2026-10-16

### Added

- Pins carry an `owner` name. The shelf page has a name field and an "Only my pins" filter.
- Archived pins can be deleted from the shelf page. The skill deletes a pin only when the user asks.

## [0.1.0] - 2026-10-16

### Added

- First version: the steps-shelf skill (pin steps, read ticks, stuck steps, reminders) and the shelf page source.
