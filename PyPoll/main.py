# The goal of this script is to automate the process of vote counting and determining a winner in an election. 
# Import necessary modules for the creation of a python script that analyzes the votes and calculate the required values.
# Modules were provided in the starter file. 

import csv
import os

# The next step is to determine/map out the file path for the dataset and the output of the analysis.
# The paths were also provided in the starter file. 

file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

# Initialize variables to track election data.
# This, also, was provided in the starter file and is meant to track the total number of votes cast. 

total_votes = 0

# Define lists and dictionaries to track candidate names and vote counts.

candidate_list = [] # a list to store names of candidates
candidate_votes = {} # a dictionary to store names of candidates along with their corresponding votes

# Winning Candidate and Winning Count Tracker

winning_candidate = ""
winning_count = 0

# Open the CSV file and process it (provided in the starter file)

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row (provided in the starter file). This will ensure that the count does not include the header row.
    # In other words, skipping it ensures that only rows containig data are processed. 

    header = next(reader)
    
    # Loop through each row of the dataset and process it (provided in the starter file)

    for row in reader:

        # Print a loading indicator (provided)

        print(". ", end="")

        # Increment the total vote count for each row
        # The foolowing line increments the total votes count by 1 as the script loops through the rows. 

        total_votes = total_votes + 1

        # Get the candidates name from the row

        candidate_name = row[2] # This line will extract the name of the candidate from the third column of the given dataset. 

        # If the candidate's name is not already in the candidate list, add them
        # The first step is to check if the name exists in the dictionary created.
        # If not, the name will be added to the list. 

        if not (candidate_name in candidate_votes): # checks the existance of the name in the list 
            candidate_votes[candidate_name] = 0 # adds the name to the dictionary and sets the initial vote to 0

            # Add a vote to the candidate's count

        current_votes = candidate_votes[candidate_name] # this line will get the vote count for the candidate and stores it in the current vote variable. 
        candidate_votes[candidate_name] = current_votes + 1 # this line will add 1 and associate the new count to the dictionary as the script loops through the dataset. 

# Open a text file to save the output (code provided in the starter file)

with open(file_to_output, "w") as txt_file: 

    # Print the total vote count (to terminal)

    election_results = (
        f"\nElection Results\n"
        f"------------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------------\n")
    print(election_results, end="")

    # Write the total vote count to the text file

    txt_file.write(election_results)

    # Loop through the candidates to determine vote percentages and identify the winner

    for candidate in candidate_votes: # loops through each candidate in the dictionary
        number_of_votes = candidate_votes[candidate] # gets the number of votes for the candidate
        percentage_of_votes = (number_of_votes / total_votes) * 100 # calculates the percentage of votes 

        # Update the winning candidate if this one has more votes

        if number_of_votes > winning_count: # checks if current candidate has more votes thaan the winning count
            winning_count = number_of_votes
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage

        vote_results = f"{candidate}: {percentage_of_votes:.3f}% ({number_of_votes})\n"
        print(vote_results, end="")
        txt_file.write(vote_results)

    # Generate and print winning candidate summary to the text file

    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"--------------------------\n")
    
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
