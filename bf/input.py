#!/usr/bin/env python3

import sys

from bf import BFException

class BFIOError(BFException):
    pass

class Input():
    """Input for brainfxxk.

    Attributes:
        prompt: String for prompt
        file: File object for input
    """

    prompt = None
    file = None
    buf = []

    def __init__(self, file=sys.stdin):
        self.file = file
        return

    def __str__(self):
        return ",".join(self.buf)

    def getchar(self):
        """Get one char as number. Extra letters are buffered."""
        # what should be returned when EOF?
        import sys
        if len(self.buf) == 0 and self.file:
            if self.prompt is None:
                raise BFIOError
            elif len(self.prompt) == 0:
                # import sys, os
                self.buf = list(sys.stdin.read())
                self.file = None
                # sys.stdin = open(os.devnull)
            else:
                self.buf = list(input(self.prompt))

        try:
            c = self.buf[0]
        except IndexError:
           # raise BFIOError("Input not available")
            return 0
        self.buf = self.buf[1:]
        return ord(c)
