#!/usr/bin/env python3

from bf.lexer import Lexer
from bf.inst import Instructions

class Translator():
    """Translator.

    Translate string of instructions into string of one-letter instructions."""

    cmds = (
        ">",
        "<",
        "+",
        "-",
        ".",
        ",",
        "[",
        "]"
    )

    dict = dict()

    def __init__(self, cmds=None):
        """Currnetly one char can be used for commands."""
        if cmds is None:
            cmds = self.cmds
        self.dict = dict(zip(cmds, self.cmds))
        self.lexer = Lexer(cmds)
        return

    def read(self, s):
        """Read string and return Instructions object."""
        l = self.lexer.read(s)
        i = Instructions()
        for c in l:
            i.add(self.dict[c])
        return i
