import os
import csv

# create a Path to collect data from the Resources folder
pypollcsv= os.path.join("../../RUTJER201901DATA3/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv")

# Declare Variables 
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open csv in read mode
with open(pypollcsv,newline="") as elections:

    # assign data under the csvreader variable
    csvreader = csv.reader(elections,delimiter=",") 

    # Skip the header to iterate through the actual values
    header = next(csvreader)     

    # Iterate through each row
    for row in csvreader: 

        # Count Voter ID's and store "total_votes"
        total_votes +=1

        # using the four dondidates names, when the name found using the if statement it will appears
        # and stored in a list. we can use values in the percent vote calculation in the print statement  
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

 # find the winer to creat a dictionary out of the two lists that was previously created
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

# the list of candidate(key) and the total votes(value) can be zipped together
# using a max function of the dictionary return the winner 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print summary analysis
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

# Print the summary table
print(f"Election Results")
print(f"----------------")
print(f"Total Votes: {total_votes}")
print(f"----------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------")
print(f"Winner: {key}")
print(f"----------------")

# print text

with open('election_results.txt', 'w') as text:

# Write methods to print to Elections_Results_Summary as text
    text.write(f"Election Results")
    text.write("\n")
    text.write(f"----------------")
    text.write("\n")
    text.write(f"Total Votes: {total_votes}")
    text.write("\n")
    text.write(f"-----------------")
    text.write("\n")
    text.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    text.write("\n")
    text.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    text.write("\n")
    text.write(f"Li: {li_percent:.3f}% ({li_votes})")
    text.write("\n")
    text.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    text.write("\n")
    text.write(f"----------------")
    text.write("\n")
    text.write(f"Winner: {key}")

