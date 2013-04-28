#!/usr/bin/env python3

class Instructions():
    def __init__(self, s=""):
        """Initialize Instruction object."""
        self.s = s
        self.i = 0
        return

    def add(self, c):
        """Add instruction c."""
        self.s = self.s + c
        return c

    def next(self):
        """Move pointer to next."""
        self.i += 1
        return self.i

    def get(self):
        """Get int of current pointer."""
        try:
            return self.s[self.i]
        except IndexError:
            return None

    def forward(self, c):
        """Search forward for c from current pointer.

        Find c and move pointer next to the posision.
        """
        pos = self.s.find(c, self.i)
        assert pos >= 0
        self.i = pos + 1
        return self.i

    def backward(self, c):
        """Search backward for c from current pointer.

        Find c and move pointer next to the posision.
        """
        pos = self.s.rfind(c, 0, self.i)
        assert pos >= 0
        self.i = pos + 1
        return self.i

    def __str__(self):
        from textwrap import wrap
        return "\n".join(wrap(self.s))
