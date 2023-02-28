#!/usr/bin/env python

'''
Description: Main FastQ sequence class.
Author: Siddharth Sinha (sid3345@gmail.com)
'''

import utility

# Description: Reads the input sequence file and returns the sequence object.
# Input: Input file
# Output: sequence object
def create_FastQ_sequence(fname):
    f = utility.read_file(fname)

    sequence = FastQ_sequence()

    try:
        while sequence.check_sequence(f):
            return sequence
    finally:
        f.close()

