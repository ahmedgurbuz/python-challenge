import os
import csv

# Path to collect data from the Resources folder

path = r"C:\Users\AG\Documents\SMU COURSE\SMU-DAL-DATA-PT-08-2019-U-C\02-Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv"

# Read in the CSV file
with open(path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')