
# PyPoll HW Challenge

# Modules
import os
import csv

# Set Path for file
csvpath = os.path.join("Resources","election_data.csv")

#Open csv file and set up reader
with open (csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter= ",")
	reader = csv.reader(csvfile)
	next(reader, None)

#The total number of votes cast


#A complete list of candidates who received votes


#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.



# Print Script Analysis

print('Election Results')
print('-------------------------')
print('Total Votes:')
print('-------------------------')
print('Candidates Stats')
print('-------------------------')
print('Winner:')
print('-------------------------')

# Export text file with results

#Create path for text results
output_path = 'results.txt'
with open(output_path,'w', newline = "") as datafile:

#Setup csv writer 
	csvwriter= csv.writer(datafile)

#Write Results
	csvwriter.writerow(['Election Results'])
	csvwriter.writerow(['-------------------------'])
	csvwriter.writerow('Total Votes:')
	csvwriter.writerow(['-------------------------'])
	csvwriter.writerow('Candidates Stats:')
	csvwriter.writerow(['-------------------------'])
	csvwriter.writerow('Winner:')
	csvwriter.writerow(['-------------------------'])
	