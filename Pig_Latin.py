#Importing the random and string module:
import string as st
import random as rd


#Variable of File_path and Empty list:
file_path = 'D:/Python_work/text_files/Nouns.csv'
random_noun = []


#Function to open the file and form a list:
def get_list(file_path):
	''''Opening a csv file and appending it the list'''
	with open(file_path,'r') as file:
		'''addinfg the name to the list'''
		for noun in file:
			random_noun.append(noun)


get_list(file_path)

#Flag for controlling the flow of the game:
flag = True
vowel = 'aeiou'

#Main body of the game:
while flag:
	print('\n\t`~`~`~`~`~`~`~`~`~`~`~`(( welcome to pig latin ))`~`~`~`~`~`~`~`~`~`~`~`~`')
	user = input('\n\thit enter to continue, else hit "q" to quit'.upper())
	noun = rd.choice(random_noun).lower()
	if user == '':
		if noun[0] in vowel:
			print(noun[1:] + noun[0]+ 'way', end='')
		else:
			print(noun[1:] + noun[0] + 'ay', end='')

	elif user.lower() == 'q':
		print('\n\t`~`~`~`~`~`~`(( exiting the game ))`~`~`~`~`~`~`~`')
		flag = False