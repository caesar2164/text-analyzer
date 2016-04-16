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

normal_power_diff_table, weighted_power_diff_table, binary_power_diff_table, connection_table, attribute_table = generate_tables(definitions_file, text_lines_to_analyze)

output_time = str(time.time()).split('.')[0]

normal_power_diff_name = 'normal_power_diff_table'
weighted_power_diff_name = 'weighted_power_diff_table'
binary_power_diff_name = 'binary_power_diff_table'
connection_name = 'connection_table'
attribute_name = 'attribute_table'

# Save Normal Power Differential Table
outputfile_path = output_time + '_' + normal_power_diff_name + '.csv'
print('\nSaving Normal Power Differential Table output to file: ' + outputfile_path + ' ... '),
with open(outputfile_path, 'w') as csvfile:
    writer = csv.writer(csvfile)
    [writer.writerow(r) for r in normal_power_diff_table]

print('DONE!')

# Save Weighted Power Differential Table
outputfile_path = output_time + '_' + weighted_power_diff_name + '.csv'
print('\nSaving Weighted Power Differential Table output to file: ' + outputfile_path + ' ... '),
with open(outputfile_path, 'w') as csvfile:
    writer = csv.writer(csvfile)
    [writer.writerow(r) for r in weighted_power_diff_table]

print('DONE!')

# Save Binary Power Differential Table
outputfile_path = output_time + '_' + binary_power_diff_name + '.csv'
print('\nSaving Binary Power Differential Table output to file: ' + outputfile_path + ' ... '),
with open(outputfile_path, 'w') as csvfile:
    writer = csv.writer(csvfile)
    [writer.writerow(r) for r in binary_power_diff_table]

print('DONE!')

# Save Connection Table
outputfile_path = output_time + '_' + connection_name + '.csv'
print('\nSaving Connection Table output to file: ' + outputfile_path + ' ... '),
with open(outputfile_path, 'w') as csvfile:
    writer = csv.writer(csvfile)
    [writer.writerow(r) for r in connection_table]

print('DONE!')

# Save Attribute Table
outputfile_path = output_time + '_' + attribute_name + '.csv'
print('\nSaving Attribute Table output to file: ' + outputfile_path + ' ... '),
with open(outputfile_path, 'w') as csvfile:
    writer = csv.writer(csvfile)
    [writer.writerow(r) for r in attribute_table]

print('DONE!')

print '\nFile Analysis Complete!\n'
