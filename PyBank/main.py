
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

#Create path for results in text
output_path = 'results.txt'
with open(output_path,'w', newline = "") as datafile:

#Setup csv writer 
	csv.wrtier= csv.writer(datafile)