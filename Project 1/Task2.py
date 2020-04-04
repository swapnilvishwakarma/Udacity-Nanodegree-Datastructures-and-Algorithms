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

myDict = {}
for i in calls:
    if i[0] in myDict:
        myDict[i[0]] += int(i[3])
    else:
        myDict[i[0]] = int(i[3])
    if i[1] in myDict:
        myDict[i[1]] += int(i[3])
    else:
        myDict[i[1]] = int(i[3])

longestTime = max(myDict, key=lambda x: myDict[x])
print(f'{longestTime} spent the longest time, {myDict[longestTime]} seconds, on the phone during September 2016')


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
