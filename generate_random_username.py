import collections
import random
import sys
import os


User = collections.namedtuple("User","id name surname")
users = []
# how much user names we want ? 
# list of names \ surnames 
# display in console and write in file 
# all -  * as functions *

def generate_random_name():
	# will be changed to read from file 

	names = ["Alex" , "Jon", "Andrew" , "Arnold" , "Arthur" , "Brenton" , "Bruce"," Orest","Adam","Alfred","Kriss","Daniel","Dexter","Duke","Evan","Gerald", "Graham","Howard", "James" , "Julian" , "Carl", "Xavier"]
	surnames = ["Doe" , "Wick" , "Turelas" , "Deprec" , "Ford " , "Queen" , "King " , "Smith" , "Jones " , "Miller" , "Davis" ,"Moore" , "Anderson" , "Jackson" ,"Clark" , "Walker" , "Lee" , " Brown" , "Williams ","Cooper " , "Ross"]

	n = len (names)
	m = len (surnames)
	#Debug print 
	#print("n = ",n , "m = ", m)

	i = random.randint(0,n-1)
	j = random.randint(0,m-1)
	#Debug print 
	#print("i = ",i , "j = ", j)

	users = User(i*j,(names[i]),(surnames[j]))
	print ("    Generate Name - OK")
	print (users)
	print(users.name , users.surname)		
	f_str1 = str(users)
	f_str2 = (users.name , users.surname )
	#Debug print 
	#print (f_str)
	write_to_file(f_str1,f_str2)



def write_to_file(f_str1,f_str2):
	if os.path.exists('random_name.txt'):
		file = open('random_name.txt','r+')
	else:
		file = open('random_name.txt','w')

	file.write(f_str1)
	file.write(str(f_str2))
	
	#Debug print 
	print("    Write to file - OK")
	#Close the file 
	file.close()

generate_random_name()
#write_to_file()


