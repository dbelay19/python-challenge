#this is the final working code except avarage
import os
import csv


MONTH_INDEX = 0
PROFT_INDEX = 1


budget_csv = os.path.join('Resources', 'budget_data.csv')
os.chdir(os.path.dirname(os.path.realpath(__file__)))

## initialize variables
total_months = 0
total_profit = 0
first_row_flag = True
#prev_profit = 0
#profit_change = 0
profit_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]

# to read in the CSV file
with open(budget_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    # to skip the header row
    next(csv_reader)

    # to loop through the rows
    for row in csv_reader:
        print(row)
        # increment the total number of months
        total_months += 1
        current_profit = int(row[PROFT_INDEX])
        # add to the total profit
        total_profit += current_profit

        if first_row_flag:
            first_row_flag = False
        else:
            # calculate the profit change from the previous month
            profit_change = current_profit - prev_profit
            profit_changes.append(profit_change)
       
            # check if we have a new greatest increase or decrease
            if profit_change > greatest_increase[PROFT_INDEX]:
                greatest_increase[PROFT_INDEX] = profit_change
                greatest_increase[MONTH_INDEX] = row[MONTH_INDEX]
            if profit_change < greatest_decrease[PROFT_INDEX]:
                greatest_decrease[PROFT_INDEX] = profit_change
                greatest_decrease[MONTH_INDEX] = row[MONTH_INDEX]
        
            
        #prepare for next row
        prev_profit = current_profit
        
# calculate the average profit change
average_change = sum(profit_changes) / len(profit_changes)
print(sum(profit_changes), len(profit_changes))


# format the results as a string
results = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
)

# print the results to the terminal
print(results)

# export the results to a text file
with open("financial_analysis.txt", "w") as txt_file:
    txt_file.write(results)
