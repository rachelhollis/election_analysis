# -*- coding: utf-8 -*-




# add dpendencies
import csv
dir(csv)

#####The data we need to retrieve
#Assign a variable to load and save files from a path
file_to_save=r"C:\Users\rache\OneDrive\Desktop\course work\python\election analysis\election_analysis\election_analysis.txt"
file_to_load=r'C:\Users\rache\OneDrive\Desktop\course work\python\election analysis\election_analysis\resources\election_results1.txt'

######'1. the total number of votes cast'

#initialize a total vote counter
total_votes = 0
#declare a list
candidate_options = []
#declare a dictionary
candidate_votes = {}

# Winning Candidate and Winning Count tracker
winning_candidate = ''
winning_count = 0
winning_percentage = 0


# Open the Election results and read the file
with open(file_to_load,'r') as election_data:
    file_reader = csv.reader(election_data)
    
    # read the header row
    headers=next(file_reader)
    
    # print each row in the CSV file
    for row in file_reader:
        #add to the total vote count
        total_votes += 1
        
###### a complete list of candidates who recieved votes'       
        #print the candiddate name from each row
        candidate_name = row[2]
        
        #add the unique candidate names to the list
        if candidate_name not in candidate_options:
            
            #add the candidate to the list
            candidate_options.append(candidate_name)
            
            
###### The total number of votes each candidate won'            
            #begin tracking that candiddate's vote count
            candidate_votes[candidate_name] = 0
            
        #add a vote to that candiddate's count
        candidate_votes[candidate_name] += 1

#save the results to our text file
with open(file_to_save,'w') as txt_file:
    
    #print the final vote count to the terminal
    election_results = (
        f'\nElection Results\n'
        f'----------------------\n'
        f'Total votes: {total_votes:,}\n'
        f'----------------------\n')
    
    print(election_results, end='')
    #save the final vote count to the text file
    txt_file.write(election_results)
    
###### The percentage of votes each candidate won'

    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        #. Print the candidate name and percentage of votes.
        
        candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
        print(candidate_results)
        txt_file.write(candidate_results)
        
        # determine winning winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
            
        winning_candidate_summary = (
            f'---------------------\n'
            f'Winner: {winning_candidate}\n'
            f'Winning Vote Count: {winning_count:,}\n'
            f'Winning Percentage: {winning_percentage:.1f}%\n'
            f'---------------------'
            )
    txt_file.write(winning_candidate_summary)
    


