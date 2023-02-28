#!/usr/bin/env python

'''
Description: Performs actions as per input parameter.
Author: Siddharth Sinha (sid3345@gmail.com)
'''

import sequence

# Description: Reads the input sequence file and returns the sequence count.
# Input: Input file
# Output: sequence count
def count_sequences(input_file):

    seq_reader = sequence.create_FastQ_sequence(input_file)
    seq_count = 0

    for _ in seq_reader:
        seq_count += 1
    return seq_count


# Description: Reads the input sequence file  and returns the nucleotides count.
# Input: Input file
# Output: nucleotides count
def count_nucleotide(input_file):

    nucleotide_reader = sequence.create_FastQ_sequence(input_file)
    nucleotide_count = 0

    for seq in nucleotide_reader:
        nucleotide_count += len(seq.sequence_letter)
    return nucleotide_count