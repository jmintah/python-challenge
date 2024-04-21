import os
import csv

election_data = os.path.join("/Users/jayp/Downloads/CU-VIRT-DATA-PT-02-2024-U-LOLC/03-Python/Starter_Code/PyPoll/Resources/election_data.csv")

candidates_names = []

number_of_votes = []

percentage_of_votes = []

total_number_of_votes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimeter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_number_of_votes += 1

        if row[2] not in candidates_names:
            candidates_names.append(row[2])
            index = candidates_names.index(row[2])
            number_of_votes.append(1)
        else:
            index = candidates_names.index(row[2])
            number_of_votes[index] += 1

    for votes in number_of_votes:
        percentage = (votes/total_number_of_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percentage_of_votes.append(percentage)

    winneer = max(number_of_votes)
    index = number_of_votes.index(winner)
    winner_candidate = candidates_names[index]

print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_number_of_votes)}")
print("--------------------------")

for i in range(len(candidates_names)):
print(f"{candidates_names[i]}: {str(percentage_of_votes[i])} ({str(total_number_of_votes[i])})")
print("--------------------------")
print(f"Winner: {winner_candidate}")
print("--------------------------")


output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_number_of_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))

for i in range(len(candidates_names)):
    line = str(f"{candidates_names[i]}: {str(percentage_of_votes[i])} ({str(total_number_of_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winner_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))
