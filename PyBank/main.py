import os
import csv

# Path to collect data from the Resources folder

path = r"C:\Users\AG\Documents\SMU COURSE\SMU-DAL-DATA-PT-08-2019-U-C\02-Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv"

# Read in the CSV file
with open(path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader, None)

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Sep", "Oct", "Nov", "Dec"]
    years = ["10","11","12","13", "14", "15", "16", "17"]

    total_profit = 0

    for row in csvreader:

        #Assigning values to variables with descriptive names
        date = row[0]
        profit = row[1]
        total_profit += int(profit)
    
    
    
    
    
    print("FINANCIAL ANALYSIS")
    print("-"*20)
    print(f"Total Months: {total_profit}")
    print(f"Total: ${total_profit}")
    print(f"Average  Change: ${total_profit}")
    print(f"Greatest Increase in Profits: {total_profit}")
    print(f"Greatest Decrease in Profits: {total_profit}")



