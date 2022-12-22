#PyPoll
#The dataset is composed of three columns: "Voter ID", "County", and "Candidate"
#Python script that analyzes the votes and calculates each of the following values:

#Allow creation of file path across OSs and import module for reading csv files
import os
import csv

#Change to current directory and access data from csv file
#os.chdir(os.path.dirname(__file__))
poll_csv = os.path.join("Resources", "election_data.csv")

#Export results
report = open("Analysis/poll_results.txt", "w")

#Open and read csv
with open(poll_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

#Define the header
    header = next(csv_reader)

#Variable Declaration Space
    rowcount = 0
    vcount={}
    candidates = []
    percent = 0
    winner=""
    winningvotes = 0

#The total number of votes cast
    for row in csv_reader:
        rowcount = rowcount + 1

#A complete list of candidates who received votes / total votes & percentages per candidate
        if row[2] not in candidates:
            candidates.append(row[2])
            vcount[row[2]]=0
        vcount[row[2]]+=1

        for candidate in vcount:
            votes = vcount.get(candidate)
            percent = float(votes)/float(rowcount)*100

#The winner of the election based on popular vote
            if votes > winningvotes:
                winningvotes=votes
                winner=candidate

print(f"Total Votes: {rowcount}")
print(f"{candidate}: {percent:.3f}% ({vcount})")
print(f"Winner: {winner}")
report.write(f"Election Results\n")
report.write(f"-------------------------\n")
report.write(f"Total Votes: {rowcount}\n")
report.write(f"-------------------------\n")
report.write(f"{candidate}: {percent:.3f}% ({vcount})\n")
report.write(f"-------------------------\n")
report.write(f"Winner: {winner}\n")