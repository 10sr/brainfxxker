#!/usr/bin/env python3

from bf.bf import BF

def main(init_commands=None, interactive=True, commands=None):
    bf = BF(commands)
    # r = bf.eval(init_commands)
    if init_commands:
        bf.add(init_commands)
    r = bf.run()
    print(r)
    if interactive:
        while True:
            try:
                s = input(">>> ")
            except EOFError:
                break
            bf.add(s)
            r = bf.run()
            bf.print_inst()
            bf.print_array()
            print(r)
        print("Exit.")
    return

if __name__ == "__main__":
    pass
