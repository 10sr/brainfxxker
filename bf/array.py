#!/usr/bin/env python3

class Array():
    def __init__(self):
        self.reset()
        return

    def reset(self):
        """Reset array."""
        self.a = [0]
        self.i = 0
        return

    def right(self):
        """Move pointer to right."""
        self.i += 1
        if self.i == len(self.a):
            self.a.append(0)
        return self.i

    def left(self):
        """Move pointer to left."""
        self.i -= 1
        assert self.i >= 0
        return self.i

    def inc(self):
        """Increment data."""
        self.a[self.i] += 1
        return self.a[self.i]

    def dec(self):
        """Decrement data."""
        self.a[self.i] -= 1
        return self.a[self.i]

    def get(self):
        """Get current data."""
        return self.a[self.i]

    def put(self, i):
        """Put data."""
        self.a[self.i] = i
        return i

    def __str__(self):
        return "|" + "|".join(str(i) for i in self.a) + "|"
