
# PyPoll HW Challenge

# Modules
import os
import csv

# Set Path for file
csvpath = os.path.join("Resources","election_data.csv")

#Set Variables
county_candidate = []
candidate_num_votes = []
candidates_unique = []
total_votes = 0
percent_votes = []
election_winner = []

#Open csv file and set up reader
with open (csvpath, newline= "") as csvfile:
	csvreader = csv.reader(csvfile, delimiter= ",")
	reader = csv.reader(csvfile)
	next(reader, None)

	for row in reader:
#total votes
		total_votes += 1
#list candidates who received votes
		county_candidate = row[2]

		if county_candidate in candidates_unique:
			county_candidate_index = candidates_unique.index(county_candidate)
			candidate_num_votes[county_candidate_index] = candidate_num_votes[county_candidate_index]+1	
		else:
			candidates_unique.append(county_candidate)
			candidate_num_votes.append(1)

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
output_path = 'Analysis/results.txt'
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
	