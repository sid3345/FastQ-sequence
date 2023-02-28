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
        self.assertEqual(self.fastq.id, sequence_id)
        self.assertEqual(self.fastq.seq, sequence_letter)
        self.assertEqual(self.fastq.qual, quality_values)