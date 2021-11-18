# -*- coding: utf-8 -*-

#####The data we need to retrieve

import csv
dir(csv)

file_to_save='election_analysis.txt'
#with open(file_to_save,'w') as txt_file:
#    txt_file.write('Counties in the Election\n')
#    txt_file.write('--------------------------\n')
#    txt_file.write('Arapahoe\nDenver\nJefferson')


file_to_load='resources\election_results.csv'
with open(file_to_load,'r') as election_data:

    #read and analyze the data here
    file_reader = csv.reader(election_data)
    headers=next(file_reader)
    print(headers)
    

######'1. the total number of votes cast'



######'2. a complete list of candidates who recieved votes'



######'3. The percentage of votes each candidate won'



######'4. The total number of votes each candidate won'



######'5. The winner of the election based on popular vote'



#close the file
  
