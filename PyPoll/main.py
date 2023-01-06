import os
import csv
#to import the csv file
election_csv = os.path.join('Resources', 'election_data.csv')
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winning_votes = 0

# Open and read CSV file
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # to Skip the header row
    next(csv_reader)
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# to determine the winner
for candidate, votes in candidates.items():
    if votes > winning_votes:
        winner = candidate
        winning_votes = votes

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    print(f"{candidate}: {votes / total_votes * 100:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write the results to a text file
with open('election_results.txt', 'w') as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-------------------------\n")
    for candidate, votes in candidates.items():
        f.write(f"{candidate}: {votes / total_votes * 100:.3f}% ({votes})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------\n")