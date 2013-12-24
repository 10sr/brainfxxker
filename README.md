Brainfxxker
===========

A [Brainfxxk](http://en.wikipedia.org/wiki/Brainfuck) machine.


Synopsis
--------

    bf [-h] [-i] [-c string] [filename]


Options
-------

Without any argument, bf runs in interactive mode. If one argument given,
commands are read from that file.

### `-i`

Run in interactive mode even if `-c` or filenames is given.

### `-c <string>`

Run string as commands.


Special commands for interactive mode
-------------------------------------

### `q`

Quit immediately.

### `h`

Show help.

### `A`

Toggle if always print memory status.

### `I`

Toggle if always print instruction array status.

### `a`

Print current memory status.

### `i`

Print current instruction array status.

### `p`

Print current status of memory and instrution array.


Inputs
------

When not in interactive mode and commands are given from a file or `-c` option,
bf accept input normally: read stdin until EOF.
