#!/usr/bin/env python3

from brainfxxker.lexer import Lexer
from brainfxxker.inst import Instructions

class Translator():
    """Translator.

    Translate string of instructions into string of one-letter instructions.

    Attributes:
        dict: Dict of commands. Values are members of self.cmds.
        rdict: Dict of commands. Keys are members of self.cmds.
    """

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

    dict = None
    rdict = None

    def __init__(self, cmds=None):
        """Initialize Translator."""
        if cmds is None:
            cmds = self.cmds
        self.dict = dict()
        self.rdict = dict()
        for name, cmd in zip(cmds, self.cmds):
            self.update_dict(name, cmd)
        self.lexer = Lexer(cmds)
        return

    def update_dict(self, name, cmd):
        """Update dictionary of name and command.

        Args:
            name: Name of command.
            cmd: Command for name. Member of self.cmds.
        """
        assert cmd in self.cmds
        self.dict[name] = cmd
        self.rdict[cmd] = name
        return

    def decode(self, s):
        """Decode string of commands into list of self.cmds.

        Returns:
            Iterable of cmds.
        """
        l = self.lexer.read(s)
        for i in l:
            yield self.dict[i]
        raise StopIteration

    def encode(self, s):
        """Encode string or list of commands into list of commands."""
        for i in s:
            yield self.rdict[i]
        raise StopIteration
