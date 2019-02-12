import os
import csv

# create a Path to collect data from the Resources folder
pybankcsv= os.path.join("../../RUTJER201901DATA3/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv")


# Create a lists to iterate through specific rows for variables
total_months = []
total_profit = []
monthly_profit_change = []
 
# Open csv 
with open(pybankcsv,newline="") as budget:

     # Store the contents of budget_data.csv in the variable csvreader
    csvreader = csv.reader(budget,delimiter=",") 

    # Skip the header labels 
    header = next(csvreader)  

    # Iterate through the rows
    for row in csvreader: 

        # Append the total months and total profit to their corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Iterate through the profits to sum the total profits
    for i in range(len(total_profit)-1):
        
        # calculate the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
# Obtain the max and min of the the montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# using month list and index from max and min, and
# using the plus 1 at the end since month associated with change is the + 1 month or next month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print Statements

print(f"Financial_Analysis")
print("-------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# print text


with open('financial_analysis.txt', 'w') as text:
    
# Write methods to print to Financial_Analysis_Summary 
    text.write(f"Financial_Analysis")
    text.write("\n")
    text.write("-------------------")
    text.write("\n")
    text.write(f"Total Months: {len(total_months)}")
    text.write("\n")
    text.write(f"Total: ${sum(total_profit)}")
    text.write("\n")
    text.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    text.write("\n")
    text.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    text.write("\n")
    text.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

