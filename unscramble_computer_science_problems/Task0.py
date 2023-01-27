"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    sending = texts[0][0]
    receiving = texts[0][1]
    time = texts[0][2]
    print("First record of texts, {} texts {} at time {}".format(sending, receiving, time))


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    sending = calls[len(calls) - 1][0]
    receiving = calls[len(calls) - 1][1]
    time = calls[len(calls) - 1][2]
    duration = calls[len(calls) - 1][3]
    print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(sending, receiving, time, duration))

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""