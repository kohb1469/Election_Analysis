#The data we need to retrieve
import csv
import os

# Create a filename variable to a direct path to the file
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)



# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:
#write something into file

    txt_file.write("Arapahoe, ")
    txt_file.write("Denver, ")
    txt_file.write("Jefferson")
#1. Total number of votes cast
#2. A complete list of condidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won 
#5. The winner of the election based on popular vote.

#close file
#election_data.close()
