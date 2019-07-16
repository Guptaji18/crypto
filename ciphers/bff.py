#!/usr/bin/env python

import sys


def char2bf(char):
    """Convert a char to brainfuck code that prints that char."""

    result_code = ""
    ascii_value = ord(char)
    #print(ascii_value)
    factor = int(ascii_value / 10)
    #print(factor)
    remaining = int(ascii_value % 10)
    #print(remaining)

    result_code += "%s\n" % ("+" * 10)
    result_code += "[\n"
    result_code += "  >\n"
    result_code += "  %s\n" % ("+" * factor)
    result_code += "  <\n"
    result_code += "  -\n"
    result_code += "]\n"
    result_code += ">\n"
    result_code += "%s\n" % ("+" * remaining)
    result_code += ".\n"
    result_code += "[-]\n"
    #print(result_code)
    return result_code


def str2bf(string):
    """Convert a string to brainfuck code that prints that string."""

    result = ""
    for char in string:
        result += char2bf(char)

    return result




