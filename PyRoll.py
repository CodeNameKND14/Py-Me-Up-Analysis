import csv
import os

pyroll_csv = os.path.join("..", "03-Python_homework_PyPoll_Resources_election_data.csv")
pyroll_output = os.path.join("election_analysis.txt")

# Total Vote Counter
total_votes = 0

# Candidate Options and Vote Counters
candidate_options = []
candidates = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = []
winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open(pyroll_csv, "r") as election_data:

    # Read in header
    reader = csv.reader(election_data)
    header = next(reader)

    # For each row ...
    for row in reader:
        # Run the loader animation
        # print(". ", end=""),

        # Add to the total vote count
        total_votes += 1

        # extract the candidate name from each row
        name = row[2]

        # If the candidate does not match any existing candidate ...
        if name not in candidate_options:

            # Append it to the list of candidates in the running
            candidate_options.append(name)

            #  Begin tracking that candidate's voter count
            candidates[name] = 0
        # Add a vote to that candidate's count each time it appears
        candidates[name] += 1

# Print the results and export the data to text file
with open(pyroll_output, "w") as txt_file:

    # Print the final vote count
    election_results = (
        f"\nElection Results"
        f"\n----------------------"
        f"\nTotal Votes: ${total_votes:,.3f}")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the winner by looping through the counts
    for candidate in candidates:

        # Retrieve vote count and percentage
        votes = candidates.get(candidate)
        print(votes)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count and percentage
        voter_output = f"{candidate}: {vote_percentage:,.3f}% ({votes:,.1f})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"--------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
