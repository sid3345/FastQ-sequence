#!/usr/bin/env python

'''
Description: Main FastQ sequence class.
Author: Siddharth Sinha (sid3345@gmail.com)
'''

import utility
import sys

# Description: Reads the input sequence file and yields the sequence object.
# Input: Input file
# Output: sequence object
def create_FastQ_sequence(fname):
    f = utility.read_file(fname)

    sequence = FastQ_sequence()

    try:
        while sequence.check_sequence(f):
            yield sequence
    finally:
        f.close()


'''Class to save FastQ sequence ID, sequence letters and quality values.'''
class FastQ_sequence():

    def __init__(self, sequence_id=None, sequence_letter=None, quality=None):
        self.sequence_id = sequence_id
        self.sequence_letter = sequence_letter
        self.quality = quality