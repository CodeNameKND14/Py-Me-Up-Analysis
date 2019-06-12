import os
import csv

pyroll_csv = os.path.join("..", "03-Python_homework_PyPoll_Resources_election_data.csv")

csvfile = open(pyroll_csv, "r")
textfile = open("PyRoll.txt", "w")
csvreader = csv.reader(csvfile, delimiter=",")
header = next(csvreader)

khan = 0
correy = 0
li = 0
tooley = 0
amount = []
for row in csvreader:
    if row[2] == "Khan":
        khan += 1
        amount.append(row[2])

    elif row[2] == "Correy":
        correy += 1
        amount.append(row[2])

    elif row[2] == "Li":
        li += 1
        amount.append(row[2])

    elif row[2] == "O'Tooley":
        tooley += 1
        amount.append(row[2])


total_votes = khan + correy + li + tooley

khan_percentage = round(khan / total_votes * 100, 2)

correy_percentage = round(correy / total_votes * 100, 2)

li_percentage = round(li / total_votes * 100, 2)

tooley_perentage = round(tooley/total_votes * 100, 2)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print(f"Khan: {khan_percentage}% ({khan})")
print(f"Correy: {correy_percentage}% ({correy})")
print(f"Li: {li_percentage}% ({li}) ")
print(f"O'Tooley': {tooley_perentage}% ({tooley}) ")
print("-------------------------")
print("Winner: Khan")
print("-------------------------")

out_put = os.path.join("PyRoll.txt")

textfile.write("Election Results\n")
textfile.write("-------------------------\n")
textfile.write(f"Total Votes: {total_votes}\n")
textfile.write(f"Khan: {khan_percentage}% ({khan})\n")
textfile.write(f"Correy: {correy_percentage}% ({correy})\n")
textfile.write(f"Li: {li_percentage}% ({li}) \n")
textfile.write(f"O'Tooley': {tooley_perentage}% ({tooley}) \n")
textfile.write("-------------------------\n")
textfile.write("Winner: Khan\n")
textfile.write("-------------------------\n")


csvfile.close()
textfile.close()
