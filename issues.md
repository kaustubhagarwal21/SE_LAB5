# Static Code Analysis – Issues Log

| Tool | Severity | Code | Line(s) | Description | Fix Approach | Status |
|------|-----------|------|---------|--------------|---------------|--------|
| Bandit | Medium | B307 | 59 | Insecure `eval()` usage | Replace with `ast.literal_eval` or safe alternative | To fix |
| Bandit | Low | B110 | 19 | Bare `try/except/pass` hides errors | Catch specific exception (e.g., `KeyError`) | To fix |
| Pylint | — | W0102 | 8 | Mutable default list argument | Use `None` default and initialize inside function | To fix |
| Pylint | — | W1514 / R1732 | 26, 32 | `open()` missing context manager & encoding | Use `with open(..., encoding="utf-8")` | To fix |
| Flake8 | — | E722 | 19 | Bare `except` | Replace with specific exception type | To fix |

| Tool   | Severity | Code           | Line(s) | Description                      | Fix Approach                                  | Status    |
|--------|----------|----------------|---------|----------------------------------|------------------------------------------------|-----------|
| Bandit | Medium   | B307           | 59      | Insecure eval() usage            | Removed eval                                   | ✅ Fixed  |
| Bandit | Low      | B110           | 19      | Bare try/except/pass             | Catch KeyError                                 | ✅ Fixed  |
| Pylint | —        | W0102          | 8       | Mutable default list argument    | Use None, init list inside                     | ✅ Fixed  |
| Pylint | —        | W1514 / R1732  | 26, 32  | open() no encoding / no context | with open(..., encoding="utf-8")               | ✅ Fixed  |
