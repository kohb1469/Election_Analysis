"""PyPoll Homework Challenge Solution."""


import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0

# Create a list and dictionary for both candidates and countys
candidate_options = []
candidate_votes = {}


county_options = []
county_votes = {}


# Track the winning candidate, vote count, percentage, largest county, and largest vote count for county
winning_candidate = ""
winning_count = 0
winning_percentage = 0


largest_county = ""
maxCountyVotes = 0


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)           
            candidate_votes[candidate_name] = 0
       
        candidate_votes[candidate_name] += 1

   
        # If county not yet included
        if county_name not in county_options:

            county_options.append(county_name)
            county_votes[county_name] = 0

        county_votes[county_name] += 1




       



# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n"
        f"-------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county, votes in county_votes.items():
        # 6b: Retrieve the county vote count.
        numVotes = votes
        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (
            f"{county} county had {votes} votes ({vote_percentage:.1f}%)\n")
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if votes > maxCountyVotes:
            largest_county = county
            maxCountyVotes = votes

    # 7: Print the county with the largest turnout to the terminal.
    winning_county = (
        f"The county with the largest vote count is {largest_county} with {maxCountyVotes} votes\n"
        f"-------------------------\n")
    print(winning_county)
    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
