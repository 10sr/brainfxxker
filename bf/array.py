#!/usr/bin/env python3

class Array():
    def __init__(self, length):
        self.length = length
        self.reset()
        return

    def reset(self):
        self.a = [0] * self.length
        self.i = 0
        return

    def right(self):
        self.i += 1
        return self.i

    def left(self):
        self.i -= 1
        return self.i

    def inc(self):
        self.a[self.i] += 1
        return self.a[self.i]

    def dec(self):
        self.a[self.i] -= 1
        return self.a[self.i]

    def get(self):
        return self.a[self.i]

    def put(self, i):
        self.a[self.i] = i
        return i
