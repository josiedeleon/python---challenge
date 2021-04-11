
# PyPoll HW Challenge

# Modules
import os
import csv

# Set Path for file
csvpath = os.path.join("Resources","election_data.csv")

#Set Variables
voter_id = []
county = []
candidate =[]
total_votes = []
election_winner = []


#Open csv file and set up reader
with open (csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter= ",")
	reader = csv.reader(csvfile)
	next(reader, None)

	for row in reader:
		vote = row[0]
		voter_id.append(vote)
		county_candidate = row[2]
		candidate.append(county_candidate)

#The total number of votes cast
	total_votes = len(voter_id)
	print(total_votes)

#A complete list of candidates who received votes


#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.


# Print Script Analysis

print('Election Results')
print('-------------------------')
print(f'Total Votes:{total_votes}')
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
	csvwriter.writerow(f'Total Votes:{total_votes}')
	csvwriter.writerow(['-------------------------'])
	csvwriter.writerow('Candidates Stats:')
	csvwriter.writerow(['-------------------------'])
	csvwriter.writerow('Winner:')
	csvwriter.writerow(['-------------------------'])
	