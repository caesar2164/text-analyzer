#!/usr/bin/env python
import yaml
import csv
import time

import setup
textfile_path, deffile_path = setup.get_arguments()

from functions import generate_tables

# Tell user which file is being analyzed and with which definitions
analyzing = "\nAnalyzing '{textfile}' using definitions from '{deffile}'".format(
    textfile=textfile_path,
    deffile=deffile_path
)
print analyzing

# Open file to be analyzed
with open(textfile_path, "r") as textfile:
    text_lines_to_analyze=textfile.readlines()

# Open definition file to use as search keys
with open(deffile_path, 'r') as stream:
    definitions_file = yaml.load(stream)

connection_table, attribute_table = generate_tables(definitions_file, text_lines_to_analyze)

output_time = str(time.time()).split('.')[0]

connection_name = 'connection_table'
attribute_name = 'attribute_table'

# Save Connection Table
outputfile_path = connection_name + '_' + output_time + '.csv'
print('\nSaving Connection Table output to file: ' + outputfile_path + ' ... '),
with open(outputfile_path, 'w') as csvfile:
    writer = csv.writer(csvfile)
    [writer.writerow(r) for r in connection_table]

print('DONE!')

# Save Attribute Table
outputfile_path = attribute_name + '_' + output_time + '.csv'
print('\nSaving Attribute Table output to file: ' + outputfile_path + ' ... '),
with open(outputfile_path, 'w') as csvfile:
    writer = csv.writer(csvfile)
    [writer.writerow(r) for r in attribute_table]

print('DONE!')

print '\nFile Analysis Complete!\n'
