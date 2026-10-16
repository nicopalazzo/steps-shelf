# Changelog

All notable changes to steps-shelf. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Screenshots of the shelf page (sample data) in the README.
- Repository standards: licence, contributing guide, security note, issue and PR templates, a `check` workflow and a secret scan.

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
