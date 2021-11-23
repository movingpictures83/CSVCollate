# CSVCollate
# Language: Python
# Input: TSV
# Output: CSV
# Tested with: PluMA 1.1, Python 3.6
# Dependency:

PluMA plugin that takes a set of CSV files and collates results based on sample labels.

The plugin takes as input a TSV file (tab-delimited) keyword-value pairs:

data: TSV file that contains a list of CSV files to collate
startrow
endrow
startcol
endcol

The TSV file specified as the argument to data should contain, one per row:
csvfile	DatasetName	Value

Samples are thus named at a course and fine level (i.e. dataset could be Mouse, 
value could be MaxEE=1.

The output CSV file will contain the average and standard error of all values
between rows startrow-endrow and startcol-endcol of the CSV files to collate (one
per row, for each CSV file in the "data" TSV.
