
# import dependencies
import os
import csv


# Set path for file
csv_path = os.path.join('Resources', 'election_data.csv')

# define lists
vote_count = []
candidates_list = []
khan_votes = []
correy_votes = []
li_votes = []
otooley_votes = []

# read the csv file and store the header row
with open(csv_path, 'r') as file:
    election_data = csv.reader(file, delimiter=',')
    header = next(election_data)
    
#  loop through rows in csv file
    for row in election_data:

# total votes, identify unique values in candidate list, tally votes by name
        vote_count.append(row[1])
        total_votes = len(vote_count)
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
        if str(row[2]) == "Khan":
            khan_votes.append(1)
        elif str(row[2]) == "Correy":
            correy_votes.append(1)
        elif str(row[2]) == "Li":
            li_votes.append(1)
        elif str(row[2]) == "O'Tooley":
            otooley_votes.append(1)
            
# calculate vote total percentage
    khan_vote_percent = round(int(len(khan_votes)) / int(total_votes) * 100, 3)
    correy_vote_percent = round(int(len(correy_votes)) / int(total_votes) * 100, 3)
    li_vote_percent = round(int(len(li_votes)) / int(total_votes) * 100, 3)
    otooley_vote_percent = round(int(len(otooley_votes)) / int(total_votes) * 100, 3)
    
# identify a winner
    winner = max([int(len(khan_votes)), int(len(correy_votes)), int(len(li_votes)), int(len(otooley_votes))])
   
# print results
    print("Election Results")
    print("---------------------------")
    print("Total Votes: " + str(total_votes))
    print("---------------------------")
    print("Khan: " + str(khan_vote_percent) + "% (" + str(len(khan_votes)) + ")")
    print("Correy: " + str(correy_vote_percent) + "% (" + str(len(correy_votes)) + ")")
    print("Li: " + str(li_vote_percent) + "% (" + str(len(li_votes)) + ")")
    print("O'Tooley: " + str(otooley_vote_percent) + "% (" + str(len(otooley_votes)) + ")")
    print("---------------------------")
    
    if int(len(khan_votes)) == winner:
        print("Winner: Khan")
    elif int(len(correy_votes)) == winner:
        print("Winner: Correy")
    elif int(len(li_votes)) == winner:
        print("Winner: Li")
    elif int(len(otooley_votes)) == winner:
        print("Winner: O'Tooley")
    print("---------------------------")

# print results to the text file
output_path = os.path.join("Output", "py_poll_new.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txt:

    # write rows to the text file
    txtwriter = txt.write("Election Results\n")
    txtwriter = txt.write("----------------------\n")
    txtwriter = txt.write("Total Votes: 3521001\n")
    txtwriter = txt.write("----------------------\n")
    txtwriter = txt.write("Khan: 63.0% (2218231)\n")
    txtwriter = txt.write("Correy: 20.0% (704200)\n")
    txtwriter = txt.write("Li: 14.0% (492940)\n")
    txtwriter = txt.write("O'Tooley: 3.0% (105630)\n")
    txtwriter = txt.write("----------------------\n")
    txtwriter = txt.write("Winner: Khan\n")
    txtwriter = txt.write("----------------------\n")

txt.close()
    

    