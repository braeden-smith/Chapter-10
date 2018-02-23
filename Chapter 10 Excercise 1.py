#Braeden Smith Chapter 10 Excercise 1

'''
Exercise 1: Revise a previous program as follows: Read and parse the "From" lines and 
pull out the addresses from the line. Count the number of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits by 
creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse 
order and print out the person who has the most commits.
'''

fname = input('Enter file name: ')
try:
	fhandle = open(fname)
except:
	print ('File cannot be opened:', fname)
	exit()
emails = dict()
for line in fhandle:
	if line.startswith('From '):
		line = line.split()
		email = line[1]
		emails[email] = emails.get(email,0) + 1
emailslist = []
for email, count in emails.items():
	emailslist.append( (count, email) )
emailslist.sort(reverse=True)
for count, email in emailslist[:1]:
	print (email, count)