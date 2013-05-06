#!/usr/bin/env python3

from bf.array import Array
from bf.trans import Translator
from bf.inst import Instructions

class BF():
    """Brainfxxk."""

    def __init__(self, commands=None, input=""):
        self.a = Array()
        self.t = Translator(commands)
        self.i = Instructions()
        self.inputstr = input
        return

    def getchar(self):
        """Get one char from self.inputsrt."""
        raise NotImplementedError

    def reset(self):
        self.a.reset()
        self.i.reset()
        return

    def add(self, s):
        l = self.t.decode(s)
        self.i.add(l)
        return

    def run(self):
        """Run to the end."""
        # self.a.reset()
        rl = []                 # list of result in int

        # l = self.t.decode(s)
        # s = Instructions(l)

        while True:
            print(self.i)
            print(self.a)
            cmd = self.i.get()

            if cmd is None:
                break
            elif cmd == ">":
                self.a.right()
                self.i.next()
            elif cmd == "<":
                self.a.left()
                self.i.next()
            elif cmd == "+":
                self.a.inc()
                self.i.next()
            elif cmd == "-":
                self.a.dec()
                self.i.next()
            elif cmd == ".":
                rl.append(self.a.get())
                self.i.next()
            elif cmd == ",":
                self.a.put(self.getchar())
                self.i.next()
            elif cmd == "[":
                if self.a.get() == 0:
                    self.i.forward("]")
                else:
                    self.i.next()
            elif cmd == "]":
                if self.a.get() != 0:
                    self.i.backward("[")
                else:
                    self.i.next()

        return "".join(chr(i) for i in rl)
