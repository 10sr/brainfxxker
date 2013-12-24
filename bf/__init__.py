#!/usr/bin/env python3

__version__ = "0.0.1"

import sys
from builtins import input as b_input

class BFException(Exception):
    pass

from bf.bf import BF
from bf.input import Input

# how to do abotu input?
# 1. if run in noninteractively, input from stdin
# 2. if run interactively, input from stdin
# 3. if command given as stdin (sys.stdin.isatty() == False), input is not available

class _ExitInteractiveLoop(Exception):
    """Exception for exit interactive loop."""
    pass

def print_interactive_help():
    print(
        "Brainfxxk commands:\n"
        "\n"
        "  > : Move current memory pointer to right.\n"
        "  < : Move current memory pointer to left.\n"
        "  + : Increment current data.\n"
        "  - : Decrement current data.\n"
        "  . : Print current data as char.\n"
        "  , : Read one string from input (Not implemented yet).\n"
        "  [ : Jump right to nearest `]' if current data is 0.\n"
        "  ] : Jump left to nearest `[' if current data is not 0.\n"
        "\n"
        "Interactive commands:\n"
        "\n"
        "  q : Quit Brainfxxer.\n"
        "  h : Show this help.\n"
        "  A : Toggle if always print memory status before prompt.\n"
        "  I : Toggle if always print instruction array status before prompt.\n"
        "  a : Print current memory status.\n"
        "  i : Print current instruction status.\n"
        "  p : Print current stauts of memoery and instruction array."
    )
    return

def _main_interactive(bf):
    global_print_memory = False
    global_print_inst = False

    print("Brainfxxker {}".format(__version__))
    print("h for help, q for quit.")

    try:
        while True:
            try:
                s = b_input(">>> ")
            except EOFError:
                raise _ExitInteractiveLoop
            r = ""

            for i in s:
                if i == "q":
                    raise _ExitInteractiveLoop
                elif i == "h":
                    print_interactive_help()
                elif i == "A":
                    global_print_memory = not global_print_memory
                elif i == "I":
                    global_print_inst = not global_print_inst
                elif i == "a":
                    bf.print_array()
                elif i == "i":
                    bf.print_inst()
                else:
                    bf.add(i)
                    r = r + bf.run()

            print(r)
            if global_print_memory:
                bf.print_array()
            if global_print_inst:
                bf.print_inst()
    except _ExitInteractiveLoop:
        pass

    print("Exit.")
    return

def main(init_commands=None, interactive=True, commands=None, debug=False):
    # 1. -c or filename given?
    # 2. sys.stdin.isatty() ? (input is connected to tty and not a file)
    # 3. -i given?

    # TTF: input without prompt
    # TFF: input without prompt

    # TFT: input is not available
    # FFT: input is not available
    # FFF: input is not available

    # TTT: input with prompt
    # FTT: input with prompt
    # FTF: input with prompt

    # if (-c or filename given) and -i not given:
    #     input without prompt
    # elif not sys.stdin.isatty():
    #     input is not available
    # else:
    #     input with prompt

    if commands:
        print("Commands cannot be changed when in interactive mode.",
              file=sys.stderr)
        sys.exit(1)

    import sys
    isatty = sys.stdin.isatty()

    inp = Input()
    bf = BF(commands=commands, debug=debug, input=inp)

    if not interactive and init_commands:
        inp.prompt = ""
        bf.add(init_commands)
        r = bf.run()
        print(r)
        return

    if isatty:
        inp.prompt = "<<< "
    else:
        inp.prompt = None

    if init_commands:
        bf.add(init_commands)
        r = bf.run()
        print(r)

    if isatty and (interactive or not init_commands):
        # input is tty, and interactive flag explicitly given or no initial
        # command given
        return _main_interactive(bf)

    elif interactive:
        # force interactive (-i given and yet input is not tty)
        # strange case?
        return _main_interactive(bf)

    else:
        # input is not a tty and not interactive (command are given from stdin)
        bf.add(sys.stdin.read())
        r = bf.run()
        print(r)
        return

if __name__ == "__main__":
    pass
