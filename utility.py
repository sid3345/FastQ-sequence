#!/usr/bin/env python

'''
Description: Utility functions to read file.
Author: Siddharth Sinha (sid3345@gmail.com)
'''

import sys
import gzip

# Input: Input file
# Output: IO Handler
def read_file(input_file):
    if input_file is None:
        io_handler = sys.stdin

    elif input_file.endswith('.gz'): # Zip file
        try:
            # This reads the file directly without unzipping it
            io_handler=gzip.open(input_file)

        except:
            sys.exit("Error reading gzipped file: " + input_file)

    else:
        try:
            io_handler = open(input_file)
        except:
            sys.exit("Error reading file: " + input_file)

    return io_handler
    