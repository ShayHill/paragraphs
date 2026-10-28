"""See full diffs in pytest.

:author: Shay Hill
:created: 2026-10-28
"""

import pytest


def pytest_assertrepr_compare(
    config: pytest.Config, op: str, left: str, right: str
) -> list[str] | None:
    """See full error diffs"""
    del config
    if op in ("==", "!="):
        return [f"{left} {op} {right}"]
    return None
