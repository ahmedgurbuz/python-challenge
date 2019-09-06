import os
import csv

# Path to collect data from the resource

path = r"C:\Users\AG\Documents\SMU COURSE\SMU-DAL-DATA-PT-08-2019-U-C\02-Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv"

# initializing the titles and rows list  
months = [] 

# Read in the CSV file
with open(path, 'r') as budget_data:

    # Split the data on commas
    csvreader = csv.reader(budget_data, delimiter=',')

    #Skipping the header row
    header = next(csvreader, None)

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Sep", "Oct", "Nov", "Dec"]
    years = ["10","11","12","13", "14", "15", "16", "17"]

    #Assigning total profit as a variable
    total_profit = 0

    #Looping through csv file with our handle
    for row in csvreader:
        
        months.append(row)

        #Assigning values to variables with descriptive names
        date = row[0]
        profit = row[1]

        #Calculating total profit
        total_profit += int(profit)
    
    
    
    
    #Printing the final values
    print("FINANCIAL ANALYSIS")
    print("-"*20)
    print(f"Total Months: {(csvreader.line_num)-1}")
    print(f"Total: ${total_profit}")
    print(f"Average  Change: ${total_profit}")
    print(f"Greatest Increase in Profits: {total_profit}")
    print(f"Greatest Decrease in Profits: {total_profit}")



