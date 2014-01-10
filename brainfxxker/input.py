#!/usr/bin/env python3

import sys

from brainfxxker import BFException

class BFIOError(BFException):
    pass

class Input():
    """Input for brainfxxk.

    getchar() to get one letter from input buffer (self.buf).
    if the buffer is empty, inputs are got in several ways:
    If input file is given, read one letter from that.
    Else if self.prompt is None, input is not available and raise BFIOError.
    Else if self.prompt is empty string, read one letter from stdin.
    Otherwise, emit prompt and get user input.

    Attributes:
        prompt: String for prompt
        file: File object for input or None to read from stdin
    """

    prompt = None
    file = None
    buf = None

    def __init__(self, file=None):
        self.file = file
        self.buf = []
        return

    def __str__(self):
        return ",".join(self.buf)

    def getchar(self):
        """Get one char as number. Extra letters are buffered."""
        # what should be returned when EOF?
        import sys
        if len(self.buf) == 0:
            if self.file:
                self.buf.append(self.file.read(1))
            elif self.prompt is None:
                raise BFIOError
            elif len(self.prompt) == 0:
                # import sys, os
                self.buf.append(sys.stdin.read(1))
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
