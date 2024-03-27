"""Test par function.

:author: Shay Hill
:created: 2024-03-27
"""

from paragraphs import par


class TestPar:
    def test_remove_indentation(self):
        """Remove leading whitespace."""
        text = par(
            """
            Lorem ipsum dolor sit amet,"""
        )
        assert text == "Lorem ipsum dolor sit amet,"

    def test_join_lines(self):
        """Join consecutive lines with a space."""
        text = par(
            """
            Lorem ipsum dolor
            sit amet,"""
        )
        assert text == "Lorem ipsum dolor sit amet,"

    def test_separate_double_newline(self):
        """Split paragraphs on double newlines."""
        text = par(
            """
            Lorem ipsum dolor
            sit amet,

            consectetur
            adipiscing
            elit"""
        )
        assert text == "Lorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit"

    def test_ignore_leading_whitespace(self):
        """Ignore leading whitespace."""
        assert par("\n\n\n\n\t   \t\nLorem ipsum") == par("Lorem ipsum")

    def test_separate_triple_newline(self):
        """Split paragraphs on triple newlines."""
        text = par(
            """
            Lorem ipsum dolor
            sit amet,


            consectetur
            adipiscing
            elit"""
        )
        assert text == "Lorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit"

    def test_separate_many_newlines(self):
        """Treat > 2 consecutive newlines as one paragraph break."""
        text = par(
            """
            Lorem ipsum dolor
            sit amet,





            consectetur
            adipiscing
            elit"""
        )
        assert text == "Lorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit"

    def test_retain_one_trailing_newline(self):
        """Retain one trailing newline."""
        text = par(
            """
            Lorem ipsum dolor
            sit amet,
            """
        )
        assert text == "Lorem ipsum dolor sit amet,\n"

    def test_retain_two_trailing_newlines_as_one(self):
        """Retain one trailing newline if text ends with multiple newlines."""
        text = par(
            """
            Lorem ipsum dolor
            sit amet,

            """
        )
        assert text == "Lorem ipsum dolor sit amet,\n"

    def test_retain_many_trailing_newlines_as_one(self):
        """Retain multiple trailing newlines as a paragraph break."""
        text = par(
            """
            Lorem ipsum dolor
            sit amet,





            """
        )
        assert text == "Lorem ipsum dolor sit amet,\n"

    def test_convert_all_whitespace_to_space(self):
        """Convert all whitespace to a single space."""
        text = par(
            """
            Lorem\tipsum dolor
            sit\tamet,\t"""
        )
        assert text == "Lorem ipsum dolor sit amet,"

    def test_compress_consecutive_whitespace(self):
        """Convert all whitespace to a single space."""
        text = par(
            """
            Lorem\t\t\t  \t\t ipsum   dolor
            sit amet,"""
        )
        assert text == "Lorem ipsum dolor sit amet,"

    def test_remove_trailing_whitespace(self):
        """Remove trailing whitespace."""
        text = par(
            """
            Lorem ipsum dolor\t\t\t\t\t
            sit amet,   \t

            consectetur\t   adipiscing\t
            elit"""
        )
        assert text == "Lorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit"

    def test_trailing_newline_tab_delimited(self):
        """Remove trailing tab but capture trailing newline."""
        text = par(
            """
            Lorem ipsum dolor sit amet,
            \t"""
        )
        assert text == "Lorem ipsum dolor sit amet,\n"
