"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

outgoing_callers = set()
incoming_phone_numbers = set()
for call in calls:
    outgoing_callers.add(call[0])
    incoming_phone_numbers.add(call[1])

outgoing_texters = set()
incoming_text_receivers = set()
for text in texts:
    outgoing_texters.add(text[0])
    incoming_text_receivers.add(text[1])

possible_telemarketers = set()
for caller in outgoing_callers:
    if caller not in outgoing_texters and caller not in incoming_text_receivers and caller not in incoming_phone_numbers:
        possible_telemarketers.add(caller)

print("These numbers could be telemarketers:")
for number in sorted(possible_telemarketers):
    print(number)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# It takes O(N) to create a list of incoming and outgoing texts and phone calls. 
# Then it takes O(N^2) to create a list of possible telemarketers because for each number in outgoing calls, 
# it loops thorugh 3 other lists to check whether the number is in any of the 3 lists. 
# Finally it takes O(nlogn) to print the list of telemarketers.