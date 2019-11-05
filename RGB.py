#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: OCT 2019
# This program is a guessing game


def color():
    # this function uses a nested loop

    red = 0
    green = 0
    blue = 0

    # process & output
    for red in range(0, 256):
        for green in range(0, 256):
            for blue in range(0, 256):
                if (red, green, blue == 255):
                    print("RGB Value is: ({0}), ({1}), ({2})"
                          .format(red, green, blue))


if __name__ == "__main__":
    color()
