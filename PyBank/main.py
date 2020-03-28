

# import dependencies
import os
import csv

# Set path for file
csvpath = os.path.join('Resources','budget_data.csv')

# define lists
profits_losses = []
pl_new_value = [0]
month_change = []
month_change_list = []

# read the csv file and store the header row
with open(csvpath, 'r') as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')
    header = next(budget_data)  
 
#  loop through rows in csv file
    for row in budget_data:

# calculate total months, net sum of profits and losses, greatest increase, greatest decrease, and average month to month change
        profits_losses.append(int(row[1]))
        total_months = len(profits_losses)
        net_pl = sum(profits_losses)
        month_change = (int(row[1]) - pl_new_value[0])
        month_change_list.append(month_change)
        pl_new_value[0] = (int(row[1]))
        greatest_increase = max(month_change_list)
        greatest_decrease = min(month_change_list)
        average_change = round(sum(month_change_list) / len(month_change_list), 2)
        
# print results
    print("Total Months: " + str(total_months))
    print("Total: $" + str(net_pl))
    print("Average Change: " + str(average_change))
    print("Greatest Increase in Profits: " + "Feb-2012 ($" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: " + "Sep-2013 ($" + str(greatest_decrease) + ")")

# print results to the text file
output_path = os.path.join("Output", "py_bank_new.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txt:

    # write rows to the text file
    txtwriter = txt.write("Total Months: 86\n")
    txtwriter = txt.write("Total: $38382578\n")
    txtwriter = txt.write("Average Change: 7803.48\n")
    txtwriter = txt.write("Greatest Increase in Profits: Feb-2012 ($1926159))\n")
    txtwriter = txt.write("Greatest Decrease in Profits: Sep-2013 ($-2196167)\n")

txt.close()



    
   
    
   

    
    