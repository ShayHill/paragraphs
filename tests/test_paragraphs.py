#!/usr/bin/env python3
"""Test functions in paragraphs.

:author: Shay Hill
:created: 7/8/2019
"""

from paragraphs.main import par

LOREM_IPSUM = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
    dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
    sunt in culpa qui officia deserunt mollit anim id est laborum.

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
    dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
    sunt in culpa qui officia deserunt mollit anim id est laborum."""


class TestPar:
    """Test the par function."""

    def test_eliminate_leading_space(self) -> None:
        """No leading whitespace in string."""
        assert par(LOREM_IPSUM)[:5] == "Lorem"

    def test_eliminate_trailing_space(self) -> None:
        """No leading whitespace in string."""
        assert par(LOREM_IPSUM)[-8:] == "laborum."

    def test_newline(self) -> None:
        """Convert a single newline into a single space."""
        assert (
            par(
                """some
        words"""
            )
            == "some words"
        )

    def test_multiple_paragraphs(self) -> None:
        """Divide paragraphs by multiple newlines."""
        assert (
            par(
                """first
        paragraph

        second paragraph"""
            )
            == "first paragraph\n\nsecond paragraph"
        )

    def test_trailing_newline(self) -> None:
        """Leave one trailing newline (if present)."""
        assert (
            par(
                """with trailing
        """
            )
            == "with trailing\n"
        )

        assert par("""without trailing""") == "without trailing"
