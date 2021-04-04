# The data we need to retrieve.
# 1. THe total number of votes cast
# 2. A complete list of the candidates whe received votes
# 3. The percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5. The winner of the election based on popular vote.

#Add dependencies
import csv
import os

# Assign a variable for the file to load and the path.
#file_to_load = os.path.join('Resources', 'election_reults.csv')
file_to_load = 'c:/users/amcal_000/desktop/bootcamp/election/resources/election_results.csv'
#Assign a variable to save the file to a path.
file_to_save = "c:/users/amcal_000/desktop/bootcamp/election/election_analysis.txt"

#Initialize a total vote counter.
total_votes = 0

#candidate options and candidate votes.
candidate_options= []
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)

    #print each row in the CSV file
    for row in file_reader:
       #Add to the total vote count.
       total_votes += 1

       #print the candidate name from each row.
       candidate_name = row[2]

       # If the candidate does not match any existing candidate...
       if candidate_name not in candidate_options:
            #Add it to the list of candidates.
           candidate_options.append(candidate_name)

           #begin tracking that candidate's vote count.
           candidate_votes[candidate_name] = 0 
       # Add vote to that candidate's count 
       candidate_votes[candidate_name] += 1

#save the results to our text file
with open(file_to_save,"w") as txt_file:
    #Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results)
    #Save the final vote count to the text file.
    txt_file.write(election_results)
    #Determine the percentage of votes for each candidate by looping though th ecounts
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        #calculate percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #Save to texet file.
        txt_file.write(candidate_results)
        #Determine winning vote count, winning percentage, and winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            #And set winning_percentage equal to candidate's name.
            winning_candidate = candidate_name
    #Print the winning candidate's reslults to terminal.
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner:  {winning_candidate}\n"
        f'Winning Vote Count:  {winning_count:,}\n'
        f"Winning Percentage:  {winning_percentage:.1f}%\n"
        f"--------------------------\n")
    print(winning_candidate_summary)
    #save results to text file.
    txt_file.write(winning_candidate_summary)
