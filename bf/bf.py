#!/usr/bin/env python3

from bf.array import Array
from bf.lexer import Lexer

class BF():
    """Brainfxxk."""

    def __init__(self, commands=None, input="", array_len=500):
        self.a = Array(array_len)
        self.l = Lexer(commands)
        self.inputstr = input
        return

    def getchar(self):
        """Get one char from self.inputsrt."""
        raise NotImplementedError

    def read(self, s):
        """Read string and return result."""
        self.a.reset()
        rl = []                 # list of result in int

        s = self.l.read(s)

        while True:
            cmd = s.get()

            if cmd is None:
                break
            elif cmd == ">":
                self.a.right()
                s.next()
            elif cmd == "<":
                self.a.left()
                s.next()
            elif cmd == "+":
                self.a.inc()
                s.next()
            elif cmd == "-":
                self.a.dec()
                s.next()
            elif cmd == ".":
                rl.append(self.a.get())
                s.next()
            elif cmd == ",":
                self.a.put(self.getchar())
                s.next()
            elif cmd == "[":
                if self.a.get() == 0:
                    s.forward("]")
                else:
                    s.next()
            elif cmd == "]":
                if self.a.get() != 0:
                    s.backward("[")
                else:
                    s.next()

        return "".join(chr(i) for i in rl)
