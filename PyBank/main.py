import csv


# Variables for output numbers
total_amount = 0
total_month = 0
maximum = ["", 0]
minimum = ["", 0]
begining_profit = 0
change_list = []

# open CSV file, read it, but not the header
with open("Resources/budget_data.csv", "r") as input_file:
    content = csv.reader(input_file)
    next(content)

    # Loop through and check each row
    for row in content:
        # print(row)
        # exit()
        total_amount = total_amount + int(row[1])
        total_month += 1

        # Look for Max and Min
        if total_month > 1:
            change = int(row[1]) - begining_profit
            change_list.append(change)
            begining_profit = int(row[1])
            if change > maximum[1]:
                maximum[1] = change
                maximum[0] = row[0]
            if change < minimum[1]:
                minimum[1] = change
                minimum[0] = row[0]

        else:
            begining_profit = int(row[1])


avg_change = round(sum(change_list)/(total_month - 1), 2)

output = f"""
Financial Analysis
----------------------------
Total Months: {total_month}
Total: ${total_amount}
Average Change: ${avg_change}
Greatest Increase in Profits: {maximum[0]} (${maximum[1]})
Greatest Decrease in Profits: {minimum[0]} (${minimum[1]})
"""

print(output)

with open("analysis/output.txt", "w") as output_file:
    output_file.write(output)
