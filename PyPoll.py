# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won 
# 5. The winner of the election based on popular vote

import csv
import os 

#Assign a variable for the file to load and the path
#file_to_load = 'Resources/election_results.csv'
file_to_load=os.path.join("Resources","election_results.csv")

#Open the election results and read the file
#election_data = open(file_to_load,'r')
with open(file_to_load) as election_data:

    #To do: perform analysis
    #print(election_data)
    #To do: read and analyze the data
    file_reader = csv.reader(election_data)
    #print each row
    #for row in file_reader:
        #print(row)
        #print(row[0])
    #print header
    headers = next(file_reader)
    print(headers)

#Close the file
election_data.close()

#Create a filename variable to a direct or indirect path to file
file_to_save=os.path.join("analysis","election_analysis.txt")

#Using the with statement open the file as a text file
#outfile = open(file_to_save,"w")
with open(file_to_save,"w") as txt_file:

#Write some data to the file
#outfile.write("Hello World")
    txt_file.write("Hello World")
    txt_file.write("Arapahoe, Denver, Jefferson")
#outfile.close()
txt_file.close()

