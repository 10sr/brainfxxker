#!/usr/bin/env python3

class Lexer():
    """Lexer."""
    def __init__(self, cmds):
        self.cmds = cmds
        return

    def read(self, s):
        """Read string and return list of token."""
        return list(s)
