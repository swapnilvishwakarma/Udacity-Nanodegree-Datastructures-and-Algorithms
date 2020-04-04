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

DifferentPhoneNumbers = set()

for num, num2 in zip(texts, calls):
    DifferentPhoneNumbers.add(num[0])
    DifferentPhoneNumbers.add(num2[0])
    DifferentPhoneNumbers.add(num[1])
    DifferentPhoneNumbers.add(num2[1])


print("There are", len(DifferentPhoneNumbers), "different telephone numbers in the records.")


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

