#Braeden Smith Chapter 10 Excercise 2 2/8/18

'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the
messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using
a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. Note that the autograde
r does not have support for the sorted() function.
'''

name = input("Enter file:")
if len(name) < 1: 
    name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    if line.startswith("From "):
        time = line.split()[5].split(":")
        counts [time[0]] = counts.get(time[0], 0) + 1
list = list()

for key, value in counts.items():
    list.append( (key,value) )
list.sort()

for hour, counts in list:
    print (hour, counts)