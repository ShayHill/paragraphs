# paragraphs

Incorporate long strings painlessly, beautifully into Python code.

## Examples

**Easily edited, `gq`-able, `fill-paragraph`-able, comprehensive error messages.**
```python
from paragraphs import par

class SuddenDeathError(Exception):
    def __init__(self, cause: str) -> None:
        self.cause = cause

    def __str__(self):
        return par(
            f"""
            Y - e - e - e - es, Lord love you! Why should she die of
            {self.cause}? She come through diphtheria right enough the year
            before.I saw her with my own eyes.Fairly blue with it, she was.They
            all thought she was dead; but my father he kept ladling gin down
            her throat til she came to so sudden that she bit the bowl off the
            spoon. 

            What call would a woman with that strength in her have to die of
            {self.cause}?  What become of her new straw hat that should have
            come to me? Somebody pinched it; and what I say is, them as pinched
            it done her in."""
        )

raise SuddenDeathError("influenza")
```

**Nicely-formatted long string data. Spoilers for some old novels here,
but these ARE the original titles.**

```python
author2titles = {
    "Samuel Penhallow": [
        par(
            """
            The history of the wars of New-England with the Eastern Indians;
            or, a narrative of their continued perfidy and cruelty, from the
            10th of August, 1703, to the peace renewed 13th of July, 1713. And
            from the 25th of July, 1722, to their submission 15th December,
            1725, which was ratified August 5th, 1726"""
        )
    ],
    "Daniel Defoe": [
        par(
            """
            The Life and Strange Surprizing Adventures of Robinson Crusoe, Of
            York, Mariner: Who lived Eight and Twenty Years, all alone in an
            un-inhabited Island on the Coast of America, near the Mouth of the
            Great River of Oroonoque; Having been cast on Shore by Shipwreck,
            wherein all the Men perished but himself. With An Account how he
            was at last as strangely deliver'd by Pyrates"""
        ),
        par(
            """The Fortunes and Misfortunes of the Famous Moll Flanders Who was
            born in Newgate, and during a life of continu’d Variety for
            Threescore Years, besides her Childhood, was Twelve Years a Whore,
            five times a Wife (whereof once to her brother) Twelve Years a
            Thief, Eight Years a Transported Felon in Virginia, at last grew
            Rich, liv’d Honest and died a Penitent"""
        ),
    ],
}
```

## Installation
```bash
pip install paragraphs
```

## Use

```python
from paragraphs import par

PARAGRAPH = par("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
    do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
    minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex
    ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
    velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
    cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
    est laborum.""")
    
# the above is equivalent to

PARAGRAPH = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod"
    " tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim"
    " veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea"
    " commodo consequat. Duis aute irure dolor in reprehenderit in voluptate"
    " velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
    " occaecat cupidatat non proident, sunt in culpa qui officia deserunt"
    " mollit anim id est laborum.")

```

## Features

Joins lines. Removes indentation and leading whitespace.

```python
from paragraphs import par

par('''
    Lorem ipsum dolor
    sit amet,'''
)
    
# yields
Lorem ipsum dolor sit amet,
```

Separates paragraphs with double newline (`'\n\n'`).

```python
from paragraphs import par
    
par '''
    Lorem ipsum dolor
    sit amet,

    consectetur
    adipiscing
    elit'''

# yields
Lorem ipsum dolor sit amet,
<blankline>
consectetur adipiscing elit
```

Retains one trailing newline (if present).

```python
>>> par('''retains one trailing newline
... ''')
retains one trailing newline
<blankline>

>>> par('''no trailing newline''')
no trailing newline
```
