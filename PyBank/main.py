#PyBank
#The dataset is composed of two columns: "Date" and "Profit/Losses"
#Python script that analyzes the records to calculate each of the following values:

#Allow creation of file path across OSs and import module for reading csv files
import os
import csv

#Change to current directory and access data from csv file
#os.chdir(os.path.dirname(__file__))
bank_csv = os.path.join("Resources", "budget_data.csv")

#Open and read csv, then split the data on commas
with open(bank_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

#Define the header
    header = next(csv_reader)

#Variable Declaration Space
    rowcount = 1
    total = 0
    g_increase = ["", 0]
    g_decrease = ["", 99999999999999]
    net_list = []
    jan_row = next(csv_reader)
    total +=int(jan_row[1])
    previous_profit = int(jan_row[1])

#The total number of months included in the dataset
    for row in csv_reader:
        rowcount +=1

 #The net total amount of "Profit/Losses" over the entire period
        total +=int(row[1])

#The net changes in "Profit/Losses" over the entire period
        net_change = int(row[1])-previous_profit
        previous_profit = int(row[1])
        net_list +=[net_change]

#The greatest increase in profits (date and amount) over the entire period
        if net_change > g_increase[1]:
            g_increase[0]=row[0]
            g_increase[1]=net_change

#The greatest decrease in profits (date and amount) over the entire period
        if net_change < g_decrease[1]:
            g_decrease[0]=row[0]
            g_decrease[1]=net_change

#Average change of Profit/Losses in entire period, round to the nearest cent
avg_change = round((sum(net_list) / len(net_list)), 2)

#Print the analysis to the terminal
print(f"Total Months: {rowcount}")
print(f"Total: ${total}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {g_increase[0]} (${g_increase[1]})")
print(f"Greatest Decrease in Profits: {g_decrease[0]} (${g_decrease[1]})")

#Export a text file with the results
report = os.path.join("Analysis", "bank_results.txt")
with open(report, 'w') as results:
    results.write(f"Financial Analysis\n")
    results.write(f"----------------------------\n")
    results.write(f"Total Months: {rowcount}\n")
    results.write(f"Total: ${total}\n")
    results.write(f"Average Change: ${avg_change}\n")
    results.write(f"Greatest Increase in Profits: {g_increase[0]} (${g_increase[1]})\n")
    results.write(f"Greatest Decrease in Profits: {g_decrease[0]} (${g_decrease[1]})\n")