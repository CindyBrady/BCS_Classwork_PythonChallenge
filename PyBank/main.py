#Import modules os and csv
import os
import csv

#Path to Resources folder
PyBankPath = os.path.join("Resources","budget_data.csv")

#Create list to store values
profit = []
month_change = []
date = []

#Set the variables
count = 0
total_profit =0
total_change_profit = 0
initial_profit = 0

#Open CSV
with open(PyBankPath,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read header
    csv_header = next(csvreader)
    #print(f"CSV Header : {csv_header}")

    #Read each row
    for row in csvreader:
        count = count + 1
        date.append(row[0])
        profit.append(row[1])
        total_profit=total_profit + int(row[1])

        #Calc month by month profit changes
        final_profit = int(row[1])
        month_change_profit = final_profit - initial_profit

        #Store changes in list
        month_change.append(month_change_profit)
        total_change_profit = total_change_profit + month_change_profit
        initial_profit=final_profit

        #Calc avg profit changes
        average_change_profits = (total_change_profit)/(count)

        #Get min and max for profit
        greatest_increase_profits = max(month_change)
        greatest_decrease_profits = min(month_change)
        increase_date = date[month_change.index(greatest_increase_profits)]
        decrease_date = date[month_change.index(greatest_decrease_profits)]

    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

with open('analysis' '/''financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")
