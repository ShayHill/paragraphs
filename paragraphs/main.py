"""Html-like formatting of multi-line strings.

:author: Shay Hill
:created: 7/8/2019
"""

import re

# match a newline followed by any number of blank lines
_RE_PARBREAK = re.compile(r"\n\s*\n")


def par(text: str) -> str:
    r"""Html-like paragraph formatting.

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
    trail = "\n" if text.rstrip(" \t").endswith("\n") else ""
    paragraphs = _RE_PARBREAK.split(text.strip())
    paragraphs = [" ".join(x.split()) for x in paragraphs]
    return "\n\n".join(paragraphs) + trail
