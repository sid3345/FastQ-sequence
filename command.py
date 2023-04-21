#!/usr/bin/env python

'''
Description: Fetches user command line input and calls corresponding action.
Author: Siddharth Sinha (sid3345@gmail.com)
'''

import sys
import action

# input parameters format: {parameter:[default, description]}
parameters = {'count_sequences': [0, 'Counts the sequences in input file'],
              'count_nucleotide': [0,'Counts the nucleotides in input file']}

def help_doc_func(parameter):
    '''
    # Description: Menu printing format function.
    # Input: Parameters dict
    # Output: Prints formatted menu
    '''
    for each in parameter.keys():
        option_print = "--" + each

        default=parameter[each][0]
        if default == "":
            default="Not defined"

        print( f"{option_print} : {parameter[each][1]}\n")
        print(f"Default : {default:}\n")


def print_exit(message=''):
    '''
    # Description: Prints message and exit.
    # Input: Message
    # Output: Prints message and exits
    '''
    print (message)
    sys.exit(1)

# Help menu
if (sys.argv[1] in ['-h', '--h', '-help', '--help']):
    print("------------------------------------------------------------------------------")
    print("Syntax : ")
    print("python " + sys.argv[0] +  " [--count_sequences] [--count_nucleotide] INPUT_FILENAME")
    print("------------------------------------------------------------------------------")
    print("Parameters:\n")
    help_doc_func(parameters)
    print_exit()

arguments = sys.argv
PARAM=arguments[1][2:]
INPUT_FILENAME=arguments[2]

if len(sys.argv) == 1 or PARAM not in parameters:
    print_exit("Incorrect parameters. Type -h or -help for menu")

try:
    func = getattr(action, PARAM)(INPUT_FILENAME)
except AttributeError:
    print_exit(f'Parameter not found "{PARAM:s}" {INPUT_FILENAME:s}')
else:
    print(func)
    