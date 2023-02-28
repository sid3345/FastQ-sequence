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

# Description: Menu printing format function.
# Input: Parameters dict
# Output: Prints formatted menu
def help_doc_func(parameter):
 
        for each in parameter.keys():
            option_print = "--" + each

            default=parameter[each][0]
            if default == "":
                default="Not defined"

            print(" %-40s : %s \n" % (option_print, parameter[each][1]))
            print("                            Default : %s\n" %default)
        return

# Description: Prints message and exit.
# Input: Message
# Output: Prints message and exits
def print_exit(message=''):
    print (message)
    sys.exit(1)

# Help menu
if (sys.argv[1] in ['-h', '--h', '-help', '--help']):
    print("------------------------------------------------------------------------------")
    print("Syntax : ")
    print("python " + sys.argv[0] +  " [--count_sequences] [--count_nucleotide] input_filename")
    print("------------------------------------------------------------------------------")
    print("Parameters:\n")
    help_doc_func(parameters)
    print_exit()

arguments = sys.argv
param=arguments[1][2:]
input_filename=arguments[2]

if len(sys.argv) == 1 or param not in parameters:
    print_exit("Incorrect parameters. Type -h or -help for menu")

try:
    func = getattr(action, param)(input_filename)
except AttributeError:
    print_exit('Parameter not found "%s" (%s)') % (param, input_filename)
else:
    print(func)