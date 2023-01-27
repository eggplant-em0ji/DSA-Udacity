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

# PART A

unique_dialed_numbers = set()
for call in calls:
  if call[0].startswith("(080)"):
    unique_dialed_numbers.add(call[1])

unique_area_codes = set()
for number in unique_dialed_numbers:
  if number.startswith("140"):
    unique_area_codes.add("140")
  elif number.startswith("("):
    str1, str2 = number.split("(")
    str3, str4 = str2.split(")")
    unique_area_codes.add("("+str3+")")
  elif " " in number:
    unique_area_codes.add(number[0]+number[1]+number[2]+number[3])

print("The numbers called by people in Bangalore have codes:")
for area_code in sorted(unique_area_codes):
  print(area_code)

# PART B

calls_to_and_from_bangalore = 0
total_calls_from_bangalore = 0

for call in calls:
  if call[0].startswith("(080)"):
    total_calls_from_bangalore += 1
    if call[1].startswith("(080)"):
      calls_to_and_from_bangalore += 1

print(round(calls_to_and_from_bangalore / total_calls_from_bangalore * 100, 2), "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A is O(N) because it loops through all of the calls once to get unique area codes, then sorts the unique area codes for print. O(N) + O(N) = O(2N) = O(N)

# Part B is O(N) because it loops thorugh all of the calls once to determine what percentage of calls from Bangalore are to Bangalore numbers