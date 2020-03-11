#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Christine Santos and Instructor(demo)"

import sys

tokens_dict = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
    '*)': '(*',
    '-->': '<!--'
    }

token_list = list(tokens_dict.keys()) + list(tokens_dict.values()
token_list = sorted(token_list, key=len, reverse=True)

def is_nested(line):
    """Validate a single input line for correct nesting"""
    stack = []
    token_counter = 0
    while line:
        token = line[0]
        
        for t in token_list:
            if line.startswith(t):
                token = t
                break

        token_counter += 1
        line = line[len(token):]

        if token in tokens_dict.values():
            stack.append(token)
        elif token in tokens_dict.keys():
            expected_opener = tokens_dict[token]
            if stack.pop() != expected_opener:
                return "NO " + str(token_counter)
    if stack:
        return "NO " + str(token_counter)

    return "YES"

def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    print("Testing for Nesting: {}".format(args[0]))
    with open(args[0]) as ifile:
        with open('output.txt', 'w') as ofile:
            for line in ifile:
                result_str = is_nested(line)
                print(result_str)
                ofile.write(result_str + '\n')


if __name__ == '__main__':
    main(sys.argv[1:])
