
# PyBank HW Challenge

# Modules
import os
import csv

# Set Path for file
csvpath = os.path.join("Resources","budget_data.csv")

#Set Variables
month_year = []
income_expense = []
total_months= []
net_income_expense = []
average_net = []
net_change = []
average_net_change = []
max_income =[]
min_expense =[]

#Open csv file and set up reader
with open (csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter= ",")
	reader = csv.reader(csvfile)
	next(reader, None)

	for row in reader:
		months = row[0]
		month_year.append(months)
		net = int(row[1])
		income_expense.append(net)

#The total number of months included in the dataset
		total_months = len(months)
		print(total_months)

#The net total amount of "Profit/Losses" over the entire period
		net_income_expense = sum(income_expense)
		print(net_income_expense)

#The changes in "Profit/Losses" over the entire period 
	net_income_expenses = len(months)-1

	for i in range(len(income_expense)-1):
	 	net_change.append(float(income_expense[i + 1])- float(income_expense[i]))
	 	net_changes = sum(net_change)
	 	print(net_changes)
	
#The average of those changes in "Profit/Losses"
	average_net_change = net_changes/net_income_expenses
	print(average_net_change)
	
#The greatest increase in profits (date and amount) over the entire period
	max_income = income_expense[income_expense.index(max(income_expense))] - income_expense[income_expense.index(max(income_expense))-1]

#The greatest decrease in losses (date and amount) over the entire period


# Print Script Analysis

print('Financial Analysis')
print('-------------------------')
print(f'Total Months:{total_months}')
print(f'Total:{net_income_expense}')
print(f'Average Change:{(average_net_change)}')
print(f'Greatest Increase in Profits:{max_income}')
print('Greatest Decrease in Profits:')

# Export text file with results

#Create path for text results
output_path = 'results.txt'
with open(output_path,'w', newline = "") as datafile:

#Setup csv writer 
	csvwriter= csv.writer(datafile)

#Write Results
	csvwriter.writerow(['Financial Analysis'])
	csvwriter.writerow(['-------------------------'])
	csvwriter.writerow(f'Total Months:{total_months}')
	csvwriter.writerow(f'Total:{net_income_expense}')
	csvwriter.writerow(f'Average Change:${round(average_net_change,2)}')
	csvwriter.writerow(f'Greatest Increase in Profits:{max_income}')
	csvwriter.writerow('Greatest Decrease in Profits:')