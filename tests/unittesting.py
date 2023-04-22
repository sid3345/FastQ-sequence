'''
Description: Unit test script to test all the functions
Author: Siddharth Sinha (sid3345@gmail.com)
'''

import unittest
import sequence

SEQUENCE_ID= '@SEQ_ID'
SEQUENCE_LETTER='GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT'
QUALITY_VALUES="!''*((((%%^+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65"

class TestCreateFastQSequence(unittest.TestCase):
    '''Testing creating FastQ sequence'''

    def test_create_fastq_sequence_good_sequence_file(self):
        '''Description: create_fastq_sequence function is correctly reading the input sequence file and yielding the sequence object.'''
        inp_file = sequence.create_fastq_sequence('./tests/good_sequence_file')

        for each_sequence in inp_file:
            self.assertEqual(type(each_sequence), type(sequence.FastQSequence(SEQUENCE_ID, SEQUENCE_LETTER, QUALITY_VALUES)))

class TestFastQSequence(unittest.TestCase):
    '''Testing setup FastQ sequence'''
    def setUp(self):
        self.seq = sequence.FastQSequence(SEQUENCE_ID, SEQUENCE_LETTER, QUALITY_VALUES)

    def test_init(self):
        '''Description: __init__ is correctly receiving the seq_id, seq_letter, QUALITY_VALUES.'''
        self.assertEqual(self.seq.sequence_id, SEQUENCE_ID)
        self.assertEqual(self.seq.sequence_letter, SEQUENCE_LETTER)
        self.assertEqual(self.seq.quality, QUALITY_VALUES)


class TestCheckFastQSequence(unittest.TestCase):
    '''Testing checking FastQ sequence'''
    def setUp(self):
        self.fastq = sequence.FastQSequence(SEQUENCE_ID, SEQUENCE_LETTER, QUALITY_VALUES)

    def test_check_sequence(self):
        '''Description: Test if check_sequence is fetching next line from the file and Modifies sequence object correctly.'''
        file_name = './tests/good_sequence_file'
        inp_file = open(file_name, encoding="utf-8")
        seq_obj = sequence.FastQSequence()
        while seq_obj.check_sequence(inp_file):
            self.assertEqual(type(seq_obj), type(sequence.FastQSequence(SEQUENCE_ID, SEQUENCE_LETTER, QUALITY_VALUES)))
        inp_file.close()

    def test_unequal_length(self):
        '''Description: check_sequence should raise an error if seq and quality length are unequal.'''
        file_name = './tests/unequal_length_sequence_file'
        inp_file = open(file_name, encoding="utf-8")
        seq_obj = sequence.FastQSequence()
        with self.assertRaises(SystemExit) as length_exception:
            seq_obj.check_sequence(inp_file)
        self.assertEqual(True, 'length' in str(length_exception.exception).lower())
