# Reflection

**1) Easiest vs hardest fixes**
- Easiest: Removing `eval` and replacing bare `except` with `except KeyError`—straightforward one-line changes.
- Hardest: File handling + validation—needed small refactors and testing.

**2) Any false positives?**
- (Example) Pylint naming (`C0103`) flagged camelCase functions. Not a false positive, but a style preference; I accepted it and moved to snake_case.

**3) How I’d integrate static analysis**
- Run `flake8` + `bandit` locally (pre-commit hook).
- Pylint + Flake8 + Bandit in CI (fail build on High/Medium Bandit, or on Flake8 errors).

**4) Tangible improvements**
- Security risk removed (`eval`), exceptions are explicit, safer file I/O with encodings, more robust type handling, cleaner logs/strings → easier to maintain and reason about.
