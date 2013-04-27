#!/usr/bin/env python3

from bf.inst import Instructions

# is it correct to call this lexer???
class Lexer():

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
        return

    def read(self, s):
        """Read string and return Instructions object."""
        i = Instructions()
        for c in s:
            i.add(self.dict[c])
        return i
