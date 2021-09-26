# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("C:\\Users\\dwest\\MSU\\HW\\module_3\\HW03\\election-analysis\\Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("C:\\Users\\dwest\\MSU\\HW\\module_3\\HW03\\election-analysis\\analysis", "election_results.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options List
candidate_options = []
# Declare the empty candidate dictionary.
candidate_votes = {}
# Empty County List
county_list = []
# Votes per county empty dictionary.
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data) 

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]
        # County information from row 1.
        county_name = row[1]

        # If the county isn't in the list, append it.
        if county_name not in county_list:
            county_list.append(county_name)
        
        # Start tracking the votes per county
            county_votes[county_name] = 0

        # Iterate and add votes based on county
        county_votes[county_name] += 1

        # Determines the Largest County based on voters
        max_key = max(county_votes, key=county_votes.get)

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

     # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\n"
        f"County Votes:\n"
        )

    print(election_results, end="")

    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)

    # start of loop to iterate through county dictionary.
    for county_name in county_votes:
        # 1. Retrieve vote count based on county.
        c_votes = county_votes[county_name]
        # 2. Calculate the percentage of votes for county results.
        county_vote_percentage = float(c_votes) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {county_vote_percentage:.1f}% ({c_votes:,})\n")

        #  Save the county results to our text file.
        txt_file.write(county_results)

        # Print each county voter result and percentage to the terminal.
        print(county_results)

    # Formatted string printout for largest county equation.
    largest_county = (
        f"-------------------------\n"
        f"Largest County Turnout: {max_key}\n"
        f"-------------------------\n")
    print(largest_county)

    # Save the largest county results to the text file.
    txt_file.write(largest_county)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 1. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 2. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    #   print out the winning candidate, vote count and percentage to
    #   terminal.  
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)


    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)


   


















