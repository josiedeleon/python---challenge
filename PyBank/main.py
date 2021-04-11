
# PyBank HW Challenge

# Modules
import os
import csv

# Set Path for file
csvpath = os.path.join("Resources","budget_data.csv")

#Open csv file and set up reader
with open (csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter= ",")
	reader = csv.reader(csvfile)
	next(reader, None)

#The total number of months included in the dataset


#The net total amount of "Profit/Losses" over the entire period


# the changes in "Profit/Losses" over the entire period, then find the average of those changes


#The greatest increase in profits (date and amount) over the entire period


#The greatest decrease in losses (date and amount) over the entire period



# Print Script Analysis

print('Financial Analysis')
print('-------------------------')
print('Total Months:')
print('Total:')
print('Average Change:')
print('Greatest Increase in Profits:')
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
	csvwriter.writerow('Total Months:')
	csvwriter.writerow('Total:')
	csvwriter.writerow('Average Change:')
	csvwriter.writerow('Greatest Increase in Profits:')
	csvwriter.writerow('Greatest Decrease in Profits:')