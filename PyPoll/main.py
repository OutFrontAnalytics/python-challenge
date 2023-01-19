import csv

total_votes = 0
cand_dict = {}
cand_list = []


# open CSV file, read it, but not the header
with open("Resources/election_data.csv", "r") as input_file:
    content = csv.reader(input_file)
    next(content)

    # Loop through and check each row
    for row in content:
        # print(row)
        total_votes += 1
        availablecand_name = row[2]
        if availablecand_name not in cand_list:
            cand_list.append(availablecand_name)
            cand_dict[availablecand_name] = 0

        cand_dict[availablecand_name] += 1
# print(total_votes)
# print(cand_dict)
winner = max(cand_dict, key=cand_dict.get)

result = {key: round(value * 100 / total_votes, 3)
          for key, value in cand_dict.items()}
# print(result)


output = f"""

Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Charles Casper Stockham: {result['Charles Casper Stockham']}% ({cand_dict['Charles Casper Stockham']})
Diana DeGette: {result ['Diana DeGette']}% ({cand_dict['Diana DeGette']})
Raymon Anthony Doane: {result['Raymon Anthony Doane']}% ({cand_dict ['Raymon Anthony Doane']})
-------------------------
Winner: {winner}
-------------------------

"""
print(output)

with open("analysis/output_election.txt", "w") as output_file:
    output_file.write(output)
