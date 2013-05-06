#!/usr/bin/env python3

class Instructions():
    """Instruction array class."""
    def __init__(self, s=None):
        """Initialize Instruction object."""
        self.reset(s)
        return

    def reset(self, s=None):
        self.s = []
        self.i = 0
        if s:
            self.add(s)
        return

    def add(self, s=None):
        """Add instruction c."""
        if s:
            for c in s:
                self.s.append(c)
        return s

    def next(self):
        """Move pointer to next."""
        self.i += 1
        return self.i

    def get(self):
        """Get instruction of current pointer."""
        try:
            return self.s[self.i]
        except IndexError:
            return None

    def forward(self, c):
        """Search forward for c from current pointer.

        Find c and move pointer next to the posision.
        """
        while True:
            self.i += 1
            current = self.get()
            assert current
            if current == c:
                self.i += 1
                return self.i

    def backward(self, c):
        """Search backward for c from current pointer.

        Find c and move pointer next to the posision.
        """
        while True:
            self.i -= 1
            current = self.get()
            assert current
            if current == c:
                self.i += 1
                return self.i

    def __str__(self):
        string = "".join(self.s)
        from textwrap import wrap
        lines = wrap(string)
        idx = self.i
        result = []
        for l in lines:
            result.append(l)
            if idx < 70:
                idx_line = " " * idx + "^"
                result.append(idx_line)
            else:
                idx = idx - 70
        return "\n".join(result)
