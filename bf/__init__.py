#!/usr/bin/env python3

from bf.bf import BF

def main(s, commands=None):
    bf = BF(commands)
    r = bf.eval(s)
    print(r)
    return

if __name__ == "__main__":
    pass
