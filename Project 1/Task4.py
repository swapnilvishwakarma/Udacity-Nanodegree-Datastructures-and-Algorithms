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

Outgoing_Calls = set()
Receiving_Calls = set()
Text_Numbers = set()

# x[0] == outgoing calls x[1] incoming calls

# get all unique outgoing calls and receiving calls
for x in calls:
    Outgoing_Calls.add(x[0])
    Receiving_Calls.add(x[1])

# get all unique text numbers
for y in texts:
    Text_Numbers.add(y[0])
    Text_Numbers.add(y[1])


outgoingDifferentReceiving = Outgoing_Calls.difference(Receiving_Calls)
outgoingDiffReceivingAndText = outgoingDifferentReceiving.difference(Text_Numbers)
sortedOrder = list(outgoingDiffReceivingAndText)
sortedOrder.sort()

print("These numbers could be telemarketers: ")
for num in sortedOrder:
    print(num)


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

