'''
STAGE 2 of PIPELINE
Having saved the html by running it in a locally controlled browser, we can now
use BeautifulSoup to parse and extract our desired data.
'''

import os
import csv
import typing
from bs4 import BeautifulSoup

# Read contents of 'enriched.html' into string 'html'
dir_path: str = os.path.dirname(os.path.realpath(__file__))
input_file: str = dir_path+'/data1/enriched.html'
with open(input_file, 'r') as input_steam:
    html: str = input_steam.read()

# Use BeautifulSoup to find tables in html with data
# This selection criterion was determined by examining the html
# structure from data0/source.html and doing some trial and error
soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')

output_rows: typing.List = []

# Extract col names from 3rd table with headerTable class
header_tables = soup.find_all("table", {"class": "headerTable"})
header_table = header_tables[2]
header_rows = header_table.findAll('tr')
names: typing.List = []
for header_row in header_rows:
    header_columns = header_row.findAll('td')
    for header_column in header_columns:
        if len(header_column.text) > 0:
            names.append(header_column.text)
output_rows.append(names)

# Extract data from 3rd table with dataTable class
data_tables = soup.find_all("table", {"class": "dataTable"})
data_table = data_tables[2]
for table_row in data_table.findAll('tr'):
    columns = table_row.findAll('td')
    new_data_row = []
    for column in columns:
        new_data_row.append(column.text)
    output_rows.append(new_data_row)

# Almost there; need to clean up output_rows
del output_rows[1]
for i, row in enumerate(output_rows):
    if i > 0:
        del row[0]

with open(dir_path+'/data2/output.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)
