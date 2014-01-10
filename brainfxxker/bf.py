#!/usr/bin/env python3

from brainfxxker.array import Array
from brainfxxker.trans import Translator
from brainfxxker.inst import Instructions

class BF():
    """Brainfxxk.

    Attributes:
        a: Memory array.
        i: Instruction array.
    """

    def __init__(self, commands=None, debug=False, input=None):
        """
        Args:
            commands: Array of commands string. None to use original bf
                instructions.
        """
        self.debug = debug
        self.clk_count = 0
        self.a = Array()
        self.t = Translator(commands)
        self.i = Instructions()
        self.input = input
        return

    def reset(self):
        self.a.reset()
        self.i.reset()
        return

    def add(self, s):
        """Add instructions.

        Args:
            s: String or iterable of strings. If s is string, it is decoded by
            Translator. If s is other iterable object, each element must be
            chars (one size string) and they are used directly for instructions.
        """
        if isinstance(s, str):
            l = self.t.decode(s)
        else:
            l = s
        self.i.add(l)
        return

    def str_array(self):
        """Print memory array."""
        return str(self.a)

    def str_inst(self):
        """Print instruction array."""
        return str(self.i)

    def str_input(self):
        return str(self.input)

    def run(self):
        """Run to the end and return a iterable of output chars or None."""
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
                self.a.put(self.input.getchar())
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

        if len(rl) == 0:
            return None
        return (chr(i) for i in rl)
