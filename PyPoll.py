# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won 
# 5. The winner of the election based on popular vote
# Add Our dependencies
import csv
import os 
# Assign a variable to load a file from a path
#file_to_load = 'Resources/election_results.csv'
file_to_load=os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path
file_to_save=os.path.join("analysis","election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0
# Candidate Options
candidate_options = []
# Declare empty dictionary
candidate_votes = {}

# Open the election results and read the file
#election_data = open(file_to_load,'r')
with open(file_to_load) as election_data:

    # To do: perform analysis
    #print(election_data)
    # To do: read and analyze the data
    file_reader = csv.reader(election_data)
    
    # Read the header row
    headers = next(file_reader)
    # print each row
    for row in file_reader:
        #print(row)
        #print(row[0])
        # 2. Add to total vote count
        total_votes += 1
        candidate_name=row[2]
        
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        
        candidate_votes[candidate_name]+=1

    # Winning Candidate and Winning Count Tracker
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0

    # Determine the percentage of votes
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = int(votes)/int(total_votes) *100
        print(f"{candidate}: {vote_percentage:.2f}% ({votes:,})")
        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true 
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate  
    
    winning_candidate_summary = (
        f"\nElection Result\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------")
    print(winning_candidate_summary)
    
# 3. Print the total votes
print(total_votes)
# Print candidate list
print(candidate_options)
# Print candidate votes dictionary
print(candidate_votes)

# Close the file
election_data.close()

# Using the with statement open the file as a text file
#outfile = open(file_to_save,"w")
with open(file_to_save,"w") as txt_file:

    # Write some data to the file
    txt_file.write(winning_candidate_summary)

#outfile.close()
txt_file.close()

