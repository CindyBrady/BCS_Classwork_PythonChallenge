# Import modules os and csv
import os
import csv

PyPollPath = os.path.join("Resources","election_data.csv")

#Create list to store values
count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

# Open CSV

with open(PyPollPath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # Read each row
    for row in csvreader:
        count = count + 1
        candidatelist.append(row[2])
        # Create set for candidate names
    for x in set(candidatelist):
        unique_candidate.append(x)
        # Total votes
        y = candidatelist.count(x)
        vote_count.append(y)
        # Percent of votes
        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
 
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(round((vote_percent[i]),3)) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")
# Generate txt file
with open('analysis' '/''election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(round((vote_percent[i]),3)) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")
