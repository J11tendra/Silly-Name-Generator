#Importing Random module:
import random as rd


#Variable of File_path:
file_path = ''  #Enter the file path
random_names = []


#Function to open the file and form a list:
def get_list(file_path):
	''''Opening a csv file and appending it the list'''
	with open(file_path,'r') as file:
		'''addinfg the name to the list'''
		for name in file:
			random_names.append(name)


get_list(file_path)


#Function to split the first name:
def first_name():
	name = rd.choice(random_names)
	first = name.split()[0]
	return first

#Function to split the last name:
def last_name():
	name = rd.choice(random_names)
	last = name.split()[-1]
	return last


#Getting a welcome msg:
print(' `~`~`~`~`~`~`~`~`((( Welcome To Silly Name Generator )))`~`~`~`~`~`~`~`~` ')

#Creating a Flag for while loop:
flag = True

#Controlling the flow of the game:
while flag:
	user = input('\nhit "enter" to continue or "q" to quit'.title())
	if user.lower() == 'q':
		print('\n\n `~`~`~`~`~`~`~`~`(( Exiting the Game!! ))`~`~`~`~`~`~`~`~` ')
		flag = False
	
	elif user == '':
		first = first_name()
		last = last_name()
		print(f'this is first name:- {first.upper()}\nthis is last name:- {last.upper()}.'.title())

	else:
		print('invalid input, try again.')
