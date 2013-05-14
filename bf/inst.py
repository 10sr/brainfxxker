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

    def jump(self):
        """Jump to matching paren."""
        first = self.get()
        assert first == "[" or first == "]"

        depth = 0
        if first == "[":
            searching = "]"
            jump = 1            # search forward
        elif first == "]":
            searching = "["
            jump = -1           # search backward

        while True:
            self.i += jump
            current = self.get()
            if current is None:
                raise ValueError("Matching {} not found".format(searching))
            elif current == searching:
                if depth > 0:
                    depth -= 1
                    continue
                else:
                    self.i += 1
                    return self.i
            elif current == first:
                depth += 1
                continue

    def __str__(self):
        string = "".join(self.s)
        from textwrap import wrap
        lines = wrap(string)
        idx = self.i
        result = []
        for l in lines:
            result.append(l)
            if idx < 0:
                pass
            elif idx < 70:
                idx_line = " " * idx + "^"
                result.append(idx_line)
                idx = idx - 70
            else:
                idx = idx - 70
        return "\n".join(result)
