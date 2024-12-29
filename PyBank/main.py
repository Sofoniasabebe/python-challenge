# The initial step in the process of analyzing the provided financial records of the company is identify dependencies needed.
# The identified dependencies/code libraries allow for proper runtime in the script's source code. 
# For this particular project, the dependencies are provided in the PyBank Homework Starter File. 

import csv
import os

# The second step is identifying the source file/dataset to work from and the output file path where the results of the analysis will be populated.
# The file paths for both the input and output files is also provided in the starter file. 

file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

# Variables are then defined to track the financial data. 
# The first two variables are provided in the starter file. The last four more variables are coined from the project instructions. 

total_months = 0
total_net = 0
profit_loss_change = []
average_of_profit_loss_change = []
month_of_change = []
greatest_profit_increase = ["", 0]  # Variable set in a way that can combine a string and a numerical value.
greatest_profit_decrease = ["", float("inf")] # The "inf" represents an infinaitely large number. 

# Opening and reading the csv file:
# Code provided in the starter file.

with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row (code provided in the starter file)
    
    header = next(reader)

    # Extracting the first row to avoid appending to the net_change_list

    first_row = next(reader)

    # Track the total and net change. 
    total_months = total_months + 1 # This will help keep track of the total by adding it to the initial value as the upcomin loop starts to count through the dataset. 
    total_net = total_net + int(first_row[1]) #This code basically adds the value from the second column of the first row, converted to an integer, to the total_net which was initially set to 0.
    previous_net = int(first_row[1])

    # Process for each row of data (the following code processes each row of the csv file one by one)

    for row in reader:

        # Track the total

        total_months = total_months + 1

        # Track the net change
        # Started by caluculating the total_net 
        value = int(row[1]) # coverts the value from the second column into integer.
        total_net = total_net + value # adds the value to the total_net. 

        # Net change

        current_value = int(row[1]) # current row into integer
        net_change = current_value - previous_net # subtracting the previous_net from current value
        previous_net = int(row[1])
        average_of_profit_loss_change.append(net_change) # adds the net_change to keep track of the change in profit/loss
        month_of_change.append(row[1]) # keeps track of months for each change is profit/loss

        # Calculate the greatest increase in profits (month and amount)

        if net_change > greatest_profit_increase[1]:
            greatest_profit_increase[1] = net_change
            greatest_profit_increase[0] = row[0] # updates the month

        # # Calculate the greatest decrease in losses (month and amount)

        if net_change < greatest_profit_decrease[1]:
            greatest_profit_decrease[1] = net_change
            greatest_profit_decrease[0] = row[0] 

# Calculate the average net change accross the months
# I calculated the total sum of the changes and divided them by th enumber of changes. 

net_average_change = sum(average_of_profit_loss_change) / len(average_of_profit_loss_change)

# Generate output summary 
# An output string was created. Within it, f-string is used for the output lines to make sure that diffrent formats of values can be printed together without syntax errors.
# The \n was used to apply breaks (force the next text appear in a new line). 
output = (
    f"\nFinancial Analysis\n"
    f"--------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_average_change:.2f}\n" # the .2f formatts the floating point number to two decimal places. 
    f"Greatest Increase in Profits: {greatest_profit_increase[0]} (${greatest_profit_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_profit_decrease[0]} (${greatest_profit_decrease[1]})\n"
)
    
# Print to terminal

print(output)

# Write the results to a text file (code provoded in the starting file)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output) 
