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
    
    total_months = (csvreader.line_num)-1
    average_change = total_profit / total_months
    
    #Printing the final values
    print("FINANCIAL ANALYSIS")
    print("-"*20)
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {total_profit}")
    print(f"Greatest Decrease in Profits: {total_profit}")

    # Open function to create and write on the file "Results.txt"  
    file_object = open(r"C:\Users\AG\Documents\python-challenge\PyBank\Results.txt","w+")

    #Assigning each lines in results table as variable
    str1 = "FINANCIAL ANALYSIS"
    str2 = str("-"*20)
    str3 = str(f"Total Months: {total_months}")
    str4 = str(f"Total: ${total_profit}")
    str5 = str(f"Average Change: ${average_change}")
    str6 = str(f"Greatest Increase in Profits: {total_profit}")
    str7 = str(f"Greatest Decrease in Profits: {total_profit}")

    #Uniting results table and writing line by line to text file
    results = [str1 + "\n", str2 + "\n", str3 + "\n", str4 + "\n", str5 + "\n", str6 + "\n", str7 + "\n"] 
    file_object.writelines(results)
    #Closing text file
    file_object.close()