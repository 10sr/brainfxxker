#!/usr/bin/env python3

from bf.array import Array
from bf.trans import Translator
from bf.inst import Instructions

class BF():
    """Brainfxxk."""

    def __init__(self, commands=None, input="", debug=False):
        self.debug = debug
        self.clk_count = 0
        self.a = Array()
        self.t = Translator(commands)
        self.i = Instructions()
        self.inputstr = input
        return

    def getchar(self):
        """Get one char from self.inputstr."""
        raise NotImplementedError

    def reset(self):
        self.a.reset()
        self.i.reset()
        return

    def add(self, s):
        """Add instructions.

        Args:
            s: String or iterable of strings. If s is string, it is decoded by
            Translator. If s is terable, each element must be chars (one size
            string) and they are used directly for instructions.
        """
        if isinstance(s, str):
            l = self.t.decode(s)
        else:
            l = s
        self.i.add(l)
        return

    def print_array(self):
        """Print memory array."""
        print(self.a)
        return

    def print_inst(self):
        """Print instruction array."""
        print(self.i)
        return

    def run(self):
        """Run to the end."""
        rl = []                 # list of result in int

        while True:
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
                if self.a.get() <= 0:
                    self.i.jump()
                else:
                    self.i.next()
            elif cmd == "]":
                if self.a.get() != 0:
                    self.i.jump()
                else:
                    self.i.next()

            self.clk_count += 1
            if self.debug and self.clk_count % 10 == 0:
                print("Clock count: {}".format(self.clk_count))
                self.print_inst()
                self.print_array()

        return "".join(chr(i) for i in rl)
