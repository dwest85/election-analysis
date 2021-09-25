# election-analysis

# Project Overview
I used the raw elction results of a recent election to complete the following tasks:

-Calculate the total number of votes cast in the election.
-Compiled a list of candidates.
-Calculated the total number and percentage of votes each candidate received.
-Determined the winner based on the voting results.
-Wrote the results to the election_analysis.txt file.

# Data used/ Software/ Resources and Analysis Folders 
-Data Source (Resoucres): election_results.csv 
    The raw election results compiled in comma seperated value format.
-Data Source (Analysis): election_analysis.txt
    Final results written to a txt file (compiled from PyPoll.py coding)
-Software: 
Python 3.8.8, Visual Studio Code, 1.60.2
-Modules:
CSV and OS

# Summary
-election_analysis.txt results:
    -There were 369,711 total votes cast.
    -The candidates were:
        -Charles Casper Stockham
        -Diana DeGette
        -Raymon Anthony Doane
    -The candidates results based on the votes:
        -Charles Casper Stockham received 85,213 votes which made up 23.0% of the total votes.
        -Diana DeGette received 272,892 votes which made up 73.8% of the total votes.
        -Raymon Anthony Doane received 11,606 votes which made up 3.1% of the total votes.
    -The winner based on the votes:
        -Diana DeGette won the election with 73.8% of the overall votes.

# Challenge Overview
    -Iterating through the raw data to assign unique candidates in the candidate_options list.
    -Tracking the candidates unique votes and assigning into the candidate_votes dictionary.
    -Tallying the final results into a readable percentage, using the .1f% decimal output.
    -Writing the necessary information to the election_analysis.txt file.
    -Making sure all variable, for loops, and if-statements were properly indented to ensure proper execution of the code.





