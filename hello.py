#!/usr/bin/env python3

import math
import time
import os
import argparse

parser = argparse.ArgumentParser("sine")
parser.add_argument("-c", "--columns", default = os.get_terminal_size().columns, type=int)
parser.add_argument("-f", "--frequency", default = 1, type=float)
parser.add_argument("-st", "--sleep_time", default = 0.01, type=float)
parser.add_argument("-r", "--character", default = "V")
args = parser.parse_args()

i = 0
columns = args.columns - 1
frequency = args.frequency
sleep_time = args.sleep_time

char = " "
r_char = args.character
long_string = char * columns

def to_radians(angle):
    return angle * (math.pi / 180)

def replace_char(old_string, index, new_string):
    return old_string[:index] + new_string + old_string[index + 1:]

def linear_interpolation(x, x0, x1, y0, y1):
    if x1 - x0 == 0:
        return (y0 + y1) / 2
    return y0 + (x - x0) * (y1 - y0) / (x1 - x0)


while(True):
    sine = math.sin(to_radians(i / frequency))
    result = linear_interpolation(sine, -1, 1, 0, columns)
    new_string = replace_char(long_string, round(result), r_char)

    print(new_string)

    i += 1
    time.sleep(sleep_time)
