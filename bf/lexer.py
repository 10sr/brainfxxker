#!/usr/bin/env python3

class Lexer():
    """Lexer."""
    def __init__(self, cmds):
        # sort commands by length, longest first.
        self.cmds = sorted(cmds, key=len, reverse=True)
        return

    def read(self, s):
        """Read string and return iterable of token."""
        l = []
        while s:
            matched = False
            for cmd in self.cmds:
                if s.startswith(cmd):
                    l.append(cmd)
                    s = s[len(cmd):]
                    matched = True
                    break
            if not matched:
                s = s[1:]           # if no match, simply ignore and go ahead.

        return l
