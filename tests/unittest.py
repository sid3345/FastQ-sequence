'''
Description: Unit test script to test all the functions
Author: Siddharth Sinha (sid3345@gmail.com)
'''

import sys
import unittest
import sequence

sequence_id= '@SEQ_ID'
sequence_letter='GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT'
quality_values="!''*((((%%^+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65"

class Test_create_FastQ_sequence(unittest.TestCase):

    # Description: create_FastQ_sequence function is correctly reading the input sequence file and yielding the sequence object.
    def test_create_FastQ_sequence_good_sequence_file(self):
        inp_file = sequence.create_FastQ_sequence('./test_cases/good_sequence_file')

        for each_sequence in inp_file:
            self.assertEqual(each_sequence, sequence.FastQ_sequence(sequence_id, sequence_letter, quality_values))

class Test_FastQ_sequence(unittest.TestCase):
    def setUp(self):
        self.seq = sequence.FastQ_sequence(sequence_id, sequence_letter, quality_values)

    # Description: __init__ is correctly receiving the seq_id, seq_letter, quality_values.
    def test_init(self):
        self.assertEqual(self.seq.id, sequence_id)
        self.assertEqual(self.seq.seq, sequence_letter)
        self.assertEqual(self.seq.qual, quality_values)


class Test_FastQ_sequence(unittest.TestCase):
    def setUp(self):
        self.fastq = sequence.FastQ_sequence(sequence_id, sequence_letter, quality_values)

    # Description: __init__ is correctly receiving the seq_id, seq_letter, quality_values.
    def test_init(self):
        self.assertEqual(self.seq.id, sequence_id)
        self.assertEqual(self.seq.seq, sequence_letter)
        self.assertEqual(self.seq.qual, quality_values)

    # Description: Test if check_sequence is fetching next line from the file and Modifies sequence object correctly.
    def test_check_sequence(self):
        file_name = './test_cases/good_sequence_file'
        
        inp_file = open(file_name)

        seq_obj = sequence.FastQ_sequence()
        while seq_obj.check_sequence(inp_file):
            self.assertEqual(seq_obj, sequence.FastQ_sequence(sequence_id, sequence_letter, quality_values))
        inp_file.close()
        
    # Description: check_sequence should raise an error if seq and quality length are unequal.
    def test_unequal_length(self):
        with self.assertRaises(sequence.Error):
            sequence.FastQ_sequence(sequence_id, sequence_letter, quality_values[:-5])