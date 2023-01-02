#!/usr/bin/env python3
"""Html-like formatting of multi-line strings.

:author: Shay Hill
:created: 7/8/2019
"""

import re


def par(text: str) -> str:
    """
    Html-like paragraph formatting.

    :param text: any block of text indented to any level
    :return:

    * whitespace substrings converted to single spaces
    * leading whitespace removed
    * double newlines ('\n\n') split paragraphs
    * one trailing newline retained (if present)

    >>> two_paragraphs = '''
    ...     Lorem ipsum dolor
    ...     sit amet,
    ...
    ...     consectetur
    ...     adipiscing
    ...     elit'''

    >>> par(two_paragraphs)
    Lorem ipsum dolor sit amet,"
    <blankline>
    consectetur adipiscing elit"

    >>> par('''retains one trailing newline
    ... ''')
    retains one trailing newline
    <blankline>

    >>> par('''no trailing newline''')
    no trailing newline
    """
    trail = "\n" if text.rstrip(" ")[-1] == "\n" else ""
    text = re.sub(r"\n\s*\n", "\n\n", text)
    paragraphs = [x.strip() for x in text.split("\n\n")]
    return "\n\n".join([re.sub(r"\s+", " ", x) for x in paragraphs]) + trail
