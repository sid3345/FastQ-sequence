# Brief
Bioinformaticians have large FASTQ files on disk, and they’d like to be able to get information about these files. They’re able to use command-line utilities on
machines running linux.

The FASTQ format is described sufficiently well here: [FASTQ format - Wikipedia](https://en.wikipedia.org/wiki/FASTQ_format#Format) (check the “Format” section). User’s files are all for nucleotide sequences, and their sequences are not split over multiple lines. Their files may be larger than available memory on the user’s machines.
After discussing their most pressing needs, the product owner has come up with the following initial user stories and associated user acceptance tests (UATs):
1. As a user, I’d like to know how many sequences are in one of my FASTQ files, so that I can decide how to split up my work.<br>
**UAT**: A command line utility, given the path to a FASTQ file and a flag requesting the sequence count, prints to STDOUT the correct number of sequences in that file. The number of sequences corresponds to the total number of non-blank lines in the file divided by 4.

2. As a user, I’d like to know the total number of nucleotides in one of my FASTQ files, so that I know how much sequencing was done, and if I need to do more.<br> **UAT**: The command line utility created for story 1, given the path to a FASTQ file and a flag requesting the nucleotide count, prints to STDOUT the correct number of nucleotides in that file. The number of nucleotides corresponds to the total number of letters found across all field 2 lines. When running, the utility uses a similar amount of memory whatever the size of the input file.

3. As a user, I’d like the new tool to work with my gzip compressed FASTQ files directly, so I don’t have to decompress them first and waste disk space.<br>
**UAT**: The command line utility created for story 1 and 2 still satisfies those UATs given the path to a gzip compressed FASTQ file, detected by having the filename suffix “.gz”. It does not first decompress the input file to an uncompressed version on disk.

## Solution
Python scripts to read, parse and process FastQ format sequence file, according to user's input

User Stories (Tasks) tracked as [Issues](https://github.com/sid3345/FastQ-sequence/issues).

Input file should be a FastQ format file in an unzipped file (txt, etc) or a zipped (.gz) file.
The Python script will output the count of the sequences in the input file and the count of the nucleotides in the input file, according to the user's CLI input flag.
<br>For the zipped input file (.gz), it reads the file directly without unzipping it.

For help section, run `python command.py -h`

### Syntax :


- `python ./command.py --count_sequences [--count_nucleotide] input_filename`

### Parameters:

`--count_sequences`                        : Counts the sequences in the input file.

 > Default : 0

 `--count_nucleotide`                       : Counts the nucleotides in the input file.
    
 > Default : 0

### Example command:

- `python ./command.py --count_nucleotide ./tests/good_sequence_file1.gz`

- `python ./command.py --count_sequences ./tests/good_sequence_file`

### File description:
- action.py: Reads the input sequence file and returns the sequence count.
- command.py: Fetches user command line input and calls corresponding action.
- sequence.py: Main FastQ sequence class to read, parse, process, and return sequence object.
- unittesting.py: Unit test script to test all the functions
- utility.py: Utility functions to read file.
- /tests: Test files for testing.
