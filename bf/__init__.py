#!/usr/bin/env python3

__version__ = "0.0.1"

import sys

from bf.bf import BF

class ExitInteractiveLoop(Exception):
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

def main_interactive(bf):
    global_print_memory = False
    global_print_inst = False

    print("Brainfxxker {}".format(__version__))
    print("h for help, q for quit.")

    try:
        while True:
            try:
                s = input(">>> ")
            except EOFError:
                raise ExitInteractiveLoop
            r = ""

            for i in s:
                if i == "q":
                    raise ExitInteractiveLoop
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
    except ExitInteractiveLoop:
        pass

    print("Exit.")
    return

def main(init_commands=None, interactive=True, commands=None, debug=False):
    bf = BF(commands=commands, debug=debug)

    if init_commands:
        bf.add(init_commands)
    r = bf.run()
    print(r)

    if not interactive:
        return

    if commands:
        print("Commands cannot be changed when in interactive mode.",
              file=sys.stderr)
        sys.exit(1)

    main_interactive(bf)
    return

if __name__ == "__main__":
    pass
