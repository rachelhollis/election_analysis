# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:46:40 2021

@author: rache
"""

#print values 
print('Hello World')

'Data Types'
# type function determines data type
type(3)


# common separates values. this does not equal 1341
ballots = 1,341


# declaring variables
num_canidates = 3
winning_percentage = 73.81
candidate = "Diane"
won_election = True


#keywords list
## help("keywords")

"Lists"

counties = ["Arapahoe","Denver","Jefferson"]

#indexing 
print(counties[0])

print(counties[-1]) #pritns last item in the list
print(counties[-2]) #second to last
print(len(counties)) #find length of a list

#slicing
counties[0:2]

print(counties[0:2]) #does not print last index 2
print(counties[:2]) #prints first two index in a list

#add items to a list

counties.append("El Paso")
print(counties)

counties.insert(2,"El Paso") #adds item at index 2
print(counties)

# remove items to a list
counties.remove("El Paso") #removes based on value
print(counties)

counties.pop(3) #removes based on index

#change element in a list
counties[2] = "El Paso"
print(counties)


'Tuples'

counties_tuple = ('Arapahoe','Denver','Jefferson')

print(counties_tuple)
print(len(counties_tuple))
print(counties_tuple[1])


'Dictionaries'

# create dict
counties_dict = {}

# add elements to dict
counties_dict["Arapahoe"] = 422829 #voters to county
counties_dict["Denver"] = 463353
counties_dict['Jefferson'] = 432438
print(counties_dict) #prints keys and values

print(len(counties_dict))

print(counties_dict.items()) #prints keys and values 

#print keys
print(counties_dict.keys())

#print values
print(counties_dict.values())

#get a specific value
print(counties_dict.get("Denver")) #prints value from key

# Lists of Dictionaries

voting_data = []

voting_data.append({'county':'Arapahoe', 'registered_voters':422829})
voting_data.append({'county':'Denver', 'register_voters':463353})
voting_data.append({'county':'Jefferson', 'register_voters': 432438})
print(voting_data)


'create algorithm to calc % of cotes a candidate recieves'

#how many votes did you get?
my_votes = int(input("How many votes? "))

#total votes in the election
total_votes = int(input('Total votes? '))

#calc % of votes you recieved
percentage_votes = (my_votes / total_votes)*100
print('I received '+str(percentage_votes)+'% of the total votes')


'decision statements'

'if statements'

counties = ['Arapahoe','Denver','Jefferson']
if counties[1]=='Denver': ##must have == for equal
    print(counties[1])

'if-else statements'

temperature = int(input('What is the temperature oustide? '))

if temperature > 80:
    print('turn on the AC')
else:
    print('open the windows')
    
' Nested if-else statements'
# if-elif-else

#what is the score?
score = int(input('What is your test score? '))

#determine grade
if score > 90:
    print('A')
else:
    if score >= 80:
        print('B')
    else:
        if score >=70:
            print('C')
        else:
            if score >= 60:
                print('D')
            else:
                print('F')
                
'elif'

#what is the score?
score = int(input('What is your test score? '))

#determine grade
if score> 90:
    print ('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print ('C')
elif score >= 60:
    print('D')
else:
    print('F')

'Membership operators'

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

'Logical operators'

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso are not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")
    
    
'Repetition statements'

'While loop'

x = 0
while x <= 5:
    print(x)
    x = x + 1
    
'for loop'

for county in counties:
    print(county)
    
    
numbers = [0,1,2,3,4]
for num in numbers:
    print(num)

# instead of making a list use range
for num in range(5):
    print(num)

'iterate through a dictionary'

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson":432438}

#get the keys of a dictionary 
for county in counties_dict:
    print(county)

for county in counties_dict.keys(): #does the same thing
    print(county)

# get the values of a dictionary
for voters in counties_dict.values():
    print(voters)

# get key-value pairs of a dict
for county, voters in counties_dict.items():
    print(county, voters)

'iterate through a list of dictionaries'

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#prints all  dict
for county_dict in voting_data:
    print(county_dict)

# get values from a list of dict
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
     print(county_dict['registered_voters'])

# get names from a list of dict
for county_dict in voting_data:
    print(county_dict['county'])
    

'F-strings'

#previous
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

# new 
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")


'Using f-string with dict'

#old code
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties._ict.items():
    print(f'{county} count has {voters} registered voters')



# Multi line f strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)


#import the datetime class from the datetime module
import datetime as dt
#use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
#print the present time
print('the time right now is ', now)










