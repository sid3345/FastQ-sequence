# FastQ-sequence
Python scripts to read, parse and output FastQ format sequence file, according to user's input

User Stories (Tasks) tracked as Issues.

Important information:

For command syntax and descriptions, run python command.py -h:
python ./command.py -h

Syntax :
------------------------------------------------------------------------------
python ./command.py [--count_sequences] [--count_nucleotide] input_filename
------------------------------------------------------------------------------
Parameters:

 --count_sequences                        : Counts the sequences in input file

                            Default : 0

 --count_nucleotide                       : Counts the nucleotides in input file

                            Default : 0


Input file should be a FastQ format file in an unzipped file (txt, etc) or a zipped (.gz) file.
The Python script will output Count of the sequences in the input file and the Count of the nucleotides in the input file, according to the user's CLI input flag.
For zipped input file (.gz), it reads the file directly without unzipping it.

Example command:
------------------------------------------------------------------------------
python ./command.py --count_nucleotide ./test_cases/good_sequence_file1.gz

python ./command.py --count_sequences ./test_cases/good_sequence_file
------------------------------------------------------------------------------

Files:
- action.py: Reads the input sequence file and returns the sequence count.
- command.py: Fetches user command line input and calls corresponding action.
- sequence.py: Main FastQ sequence class to read, parse, process, and return sequence object.
- unit_test.py: Unit test script to test all the functions
- utility.py: Utility functions to read file.

Unable to create and perform complete test cases, in the given time, but will eventually complete it.
