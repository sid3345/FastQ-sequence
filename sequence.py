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

    # Description: Fetches next line from the file and Modifies sequence object
    # Input: sequence details
    # Output: True / False, Modifies sequence object
    def check_sequence(self, f):

        line = f.readline()
        if type(line) is not str:
            line=line.decode("utf-8")

        while line == '\n':
            line = f.readline()
            if type(line) is not str:
                line=line.decode("utf-8")

        if not line:
            return False
                
        if not line.startswith('@'):
            sys.exit('Error fetching next sequence. Line does not starts with @:\n' + line + '\n Exiting')

        self.sequence_id = line.rstrip()[1:]
        line = f.readline()
        if type(line) is not str:
            line=line.decode("utf-8")

        if not line:
            sys.exit('Error fetching sequence letter, seq ID: ' + self.sequence_id + '\n Exiting')

        self.sequence_letter = line.strip()

        line = f.readline()
        if type(line) is not str:
            line=line.decode("utf-8")

        if not (line and line.startswith('+')):
             sys.exit('Error reading next sequence. seq ID: ' + self.sequence_id + '\n Exiting')
        
        line = f.readline()
        if type(line) is not str:
            line=line.decode("utf-8")

        if not line:
            sys.exit('Error fetching quality values. seq ID: ' + self.sequence_id + '\n Exiting')

        self.quality = line.rstrip()

        if len(self.quality) != len(self.sequence_letter):
            sys.exit('Length of sequence letter and quality values not equal. seq ID: ' + self.sequence_id + '\n Exiting')
    
        return True