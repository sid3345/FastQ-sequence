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
        self.fastq = sequence.FastQ_sequence(sequence_id, sequence_letter, quality_values)