"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

numbers_call_length = {}

for caller, receiver, time, duration in calls:
    if caller not in numbers_call_length:
        numbers_call_length[caller] = int(duration)
    else:
        numbers_call_length[caller] += int(duration)
    if receiver not in numbers_call_length:
        numbers_call_length[receiver] = int(duration)
    else:
        numbers_call_length[receiver] += int(duration)

max_caller = max(numbers_call_length, key=numbers_call_length.get)
max_duration = max(numbers_call_length.values())

print(max_caller, "spend the longest time,", max_duration, "seconds, on the phone during September 2016.")