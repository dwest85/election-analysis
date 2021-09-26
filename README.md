# election-analysis

# Project Overview
I used the raw elction results of a recent Colorado-based election to complete the following tasks:

1. Calculate the total number of votes cast in the election.
2. Compiled a list of candidates.
3. Calculated the total number and percentage of votes each candidate received.
4. Determined the winner based on the voting results.
5. Iterate through the voting results to seperate county votes.
6. Discover the largest voting county based on the results.
7. Wrote the results to the election_analysis.txt file.

# Data used/ Software/ Resources and Analysis Folders 
1. Data Source (Resoucres): election_results.csv
    The raw election results compiled in comma seperated value format.
2. Data Source (Analysis): election_analysis.txt
    Final results written to a txt file (compiled from PyPoll.py coding)
3. Software:
    Python 3.8.8, Visual Studio Code, 1.60.2
4. Modules:
    CSV and OS

# Election-Audit Results
* There were 369,711 total votes cast. The votes were iterated through and pulled from election_results.csv based on:
Candidate vote and County where the vote was placed.
![votescast](https://github.com/dwest85/election-analysis/blob/main/markdownpics/votescast.JPG)
* Based on the county results: Denver had the most votes placed with 82.8%, second was Jefferson with 10.5%, and lastly Arapahoe with 6.7%. 
These results were brokedown from the following algorithm with iterating the data through the election_results.csv source.
![countyvotesbreakdown](https://github.com/dwest85/election-analysis/blob/main/markdownpics/countyvotesbreakdown.JPG)
* Denver had the largest number of votes: 306,055 (82.8%). The following code below was used to determine the largest amount of votes by county.

![largestcountyvote](https://github.com/dwest85/election-analysis/blob/main/markdownpics/largestcountyvote.JPG)
* The votes were compiled into an empty dictionary with the keys being the candidates. That data was then passed into the following algorithm to 
to find each candidate's number of votes and the percentage of those votes.
![candidatevotebreakdown](https://github.com/dwest85/election-analysis/blob/main/markdownpics/candidatevotebreakdown.JPG) 
* Diana Degette won the election with 73.8% of the votes (272,892). The following code below explains the process of finding the winner and printing those results.
![winnerbreakdwon](https://github.com/dwest85/election-analysis/blob/main/markdownpics/winnerbreakdown.JPG)


# General Summary
1. election_analysis.txt results:
2. There were 369,711 total votes cast.
3. The candidates were:
    -Charles Casper Stockham
    -Diana DeGette
    -Raymon Anthony Doane
4. The candidates results based on the votes:
    -Charles Casper Stockham received 85,213 votes which made up 23.0% of the total votes.
    -Diana DeGette received 272,892 votes which made up 73.8% of the total votes.
    -Raymon Anthony Doane received 11,606 votes which made up 3.1% of the total votes.
5. The winner based on the votes:
    -Diana DeGette won the election with 73.8% of the overall votes.

# Challenge Overview
    1. Iterating through the raw data to assign unique candidates in the candidate_options list.
    2. Tracking the candidates unique votes and assigning into the candidate_votes dictionary.
    3. Tallying the final results into a readable percentage, using the .1f% decimal output.
    4. Writing the necessary information to the election_analysis.txt file.
    5. Making sure all variable, for loops, and if-statements were properly indented to ensure proper execution of the code.


# Election-Audit Summary
Overall, the script created for this election can be modified for any future elections by changing the variables used and the destination of where the values are being pulled from (raw data). Some examples of using this script for future use would be: Voting on proposal plans based on all counties, or it could be modified to even poll votes for social events in those counties.  





