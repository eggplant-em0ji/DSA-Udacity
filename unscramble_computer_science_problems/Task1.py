"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
unique_numbers = set()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for record in texts + calls:
        unique_numbers.add(record[0])
        unique_numbers.add(record[1])

print("There are", len(unique_numbers), "different telephone numbers in the records.")


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""