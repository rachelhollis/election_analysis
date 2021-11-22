# election_analysis

## Overview 
The following tasks were given to complete the election audit of a local election
- Calculate the total votes cast
- Get a complete list of candidates
- Calculate the total votes for each candidate
- Calculate the percentages of votes each candidate recieved
- Get a complete list of counties that had ballots
- Calculate the voter turnout for each county (number of votes per county)
- Determing the county with the highest turnout
- Determine the winner of the election

## Purpose

Perform analysis on the election audit results. Specifically, use Python to analyze the large data set and determine the winner of the election and the county that has the highest voter turnout. Additionally, the use of python will help to further obtain specific data in regards to the candidates and counties in the election audit.

## Election-Audit Results:

### County Analysis

![resources/total_votes](resources/total_votes.jpg)
- A for loop was used to determine the total votes in the election data set. Every row was counted as one vote. There was a total of 369,711 votes in the election audit.

![resources/candidate_votes](resources/candidate_votes.jpg)

- In the python script, inside the for loop from row 42, an if statement was used to determine the specific counties that had votes cast as well as how many votes per county. 
  - Jefferson: 38,855 votes
  - Denver: 306,055 votes
  - Arapahoe: 24,801 votes

![resources/county_results](resources/county_results.jpg)

- Lines 97 - 104 calculated the percentage of votes each county received out of the total 369,711 votes.
  - Jefferson: 10.5% percent of the total votes
  - Denver: 82.8% of the total votes
  - Arapahoe: 6.7% of the total votes

- Lines 110 – 123 determined which county had the highest percentage and output the results to the text file. 
  - The county with the highest voter turnout was Denver: 82.8% (306,055)

### Candidate Analysis




## Challenge Overview

## Challenge Summary
