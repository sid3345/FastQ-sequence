#!/usr/bin/env python

'''
Description: Fetches user command line input and calls corresponding action.
Author: Siddharth Sinha (sid3345@gmail.com)
'''

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
