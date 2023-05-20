import os
import csv

filename_1 = r'D:\mentorship program\week2\translation_results_1.csv'
filename_2 = r'D:\mentorship program\week2\translation_results_2.csv'

def get_columns(filename):
    with open(filename) as file:
        reader = csv.reader(file, delimiter=",")
        lines = list(reader)
        columns = [list(x) for x in zip(*lines)]  # Transpose lines to columns
    return columns

columns_1 = get_columns(filename_1)
columns_2 = get_columns(filename_2)

set_1_0 = set(columns_1[0]) # first column in csv file 1
set_2_0 = set(columns_2[0]) # first column in csv file 2

diff_1_0 = set_1_0 - set_2_0 # elements that set_1_0 has while set_2_0 does not have
diff_2_0 = set_2_0 - set_1_0 # elements that set_2_0 has while set_1_0 does not have