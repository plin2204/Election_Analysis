# Add Our dependencies
import csv
import os 

# Assign a variable to load a file from a path
file_to_load=os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path
file_to_save=os.path.join("analysis","election_analysis.txt")

# Initialize a total vote counter
total_votes = 0
# Candidate Option List
candidate_options = []
# Candidate dictionary with votes
candidate_votes = {}
# County list
county_list = []
# County dictionary with votes
county_votes = {}

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze the data
    file_reader = csv.reader(election_data) 
    # Read the header row
    headers = next(file_reader)

    # Analyze each row
    for row in file_reader:
        # Count total vote count
        total_votes += 1
        # Read candidate and county name
        candidate_name = row[2]
        county_name = row[1]
        
        # Analyze candidates
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Save candidate name as key in dictionary
            candidate_votes[candidate_name] = 0
        # Count candidate votes as value in dictionary
        candidate_votes[candidate_name] += 1

        # Analyze counties
        if county_name not in county_list:
            county_list.append(county_name)
            # Save county name as key in dictionary
            county_votes[county_name] = 0
        # Count county votes as value in dictionary
        county_votes[county_name] += 1

    # Winning Candidate/County and Winning Count Tracker
    winning_candidate = ""
    winning_count_candidate = 0
    winning_percentage_candidate = 0
    winning_county = ""
    winning_count_county = 0
    winning_percentage_county = 0

    # Determine the winning candidate, votes, and percentage of votes
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = int(votes)/int(total_votes) *100
        print(f"{candidate}: {vote_percentage:.2f}% ({votes:,})")
        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count_candidate):
            # 2. If true, take over winning_count and _percentage
            winning_count_candidate = votes
            winning_percentage_candidate = vote_percentage
            # 3. Set the winning_candidate as the candidate's name.
            winning_candidate = candidate  

    # Determine the winning county, votes, and percentage of votes
    for county in county_votes:
        votes = county_votes[county]
        vote_percentage = int(votes)/int(total_votes) *100
        print(f"{county}: {vote_percentage:.2f}% ({votes:,})")
        # Determine winning vote count and county
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count_county):
            # 2. If true, take over winning_count and _percentage
            winning_count_county = votes
            winning_percentage_county = vote_percentage
            # 3. Set the winning_candidate as the candidate's name.
            winning_county = county   

# 3. Print the total votes
print(total_votes)
# Print candidate list
print(candidate_options)
# Print candidate votes dictionary
print(candidate_votes)

# Close the file
election_data.close()

total_votes_summary = (
    f"\nElection Result\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"=========================\n")
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count_candidate:,}\n"
    f"Winning Percentage: {winning_percentage_candidate:.1f}%\n"
    f"-------------------------")

# Using the with statement open the file as a text file
with open(file_to_save,"w") as txt_file:

    # Write total votes of the election
    txt_file.write(total_votes_summary)
    # Write county data to the file
    txt_file.write(f"\nCounty Votes:\n")
    for county in county_votes:
        votes = county_votes[county]
        vote_percentage = int(votes)/int(total_votes) *100
        txt_file.write(f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
    txt_file.write(f"\n-------------------------\n"
                    f"Largest County Turnout: {winning_county}\n"
                    f"-------------------------\n")
    # Write candidate data to the file
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = int(votes)/int(total_votes) *100
        txt_file.write(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
    txt_file.write(winning_candidate_summary)

txt_file.close()