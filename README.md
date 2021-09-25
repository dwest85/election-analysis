# election-analysis

# Project Overview
I used the raw elction results of a recent election to complete the following tasks:

-Calculate the total number of votes cast in the election.\n
-Compiled a list of candidates.\n
-Calculated the total number and percentage of votes each candidate received.\n
-Determined the winner based on the voting results.\n
-Wrote the results to the election_analysis.txt file.\n

# Data used/ Software/ Resources and Analysis Folders 
-Data Source (Resoucres): election_results.csv\n
    The raw election results compiled in comma seperated value format.\n
-Data Source (Analysis): election_analysis.txt\n
    Final results written to a txt file (compiled from PyPoll.py coding)\n
-Software:\n 
Python 3.8.8, Visual Studio Code, 1.60.2\n
-Modules:\n
CSV and OS\n

# Summary
-election_analysis.txt results:\n
    -There were 369,711 total votes cast.\n
    -The candidates were:\n
        -Charles Casper Stockham\n
        -Diana DeGette\n
        -Raymon Anthony Doane\n
    -The candidates results based on the votes:\n
        -Charles Casper Stockham received 85,213 votes which made up 23.0% of the total votes.\n
        -Diana DeGette received 272,892 votes which made up 73.8% of the total votes.\n
        -Raymon Anthony Doane received 11,606 votes which made up 3.1% of the total votes.\n
    -The winner based on the votes:\n
        -Diana DeGette won the election with 73.8% of the overall votes.\n

# Challenge Overview
    -Iterating through the raw data to assign unique candidates in the candidate_options list.\n
    -Tracking the candidates unique votes and assigning into the candidate_votes dictionary.\n
    -Tallying the final results into a readable percentage, using the .1f% decimal output.\n
    -Writing the necessary information to the election_analysis.txt file.\n
    -Making sure all variable, for loops, and if-statements were properly indented to ensure proper execution of the code.\n





