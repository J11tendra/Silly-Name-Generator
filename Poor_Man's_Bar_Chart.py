#Dict of alphabets:
alphabet = {
	'a':[],
	'b':[],
	'c':[],
	'd':[],
	'e':[],
	'f':[],
	'g':[],
	'h':[],
	'i':[],
	'j':[],
	'k':[],
	'l':[],
	'm':[],
	'n':[],
	'o':[],
	'p':[],
	'q':[],
	'r':[],
	's':[],
	't':[],
	'u':[],
	'v':[],
	'w':[],
	'x':[],
	'y':[],
	'z':[],
	} 


#Function to clasify the string:
def clasify_string(string):
	for key in alphabet.keys():
		for letter in string:
			if key == letter:
				alphabet[key].append(letter)
	return alphabet


#Flag to make the game run and stop:
active = True


while active:
    #Asking the user for input:
    print("\n\n--------Welcome To Poor Man's Bar Chart-------")
    name = input("\nWhat's your good name?")
    string = input(f'\n{name}, enter a word.'.title())
#    print(name,'\n',string)
    user = input('hit enter to continue else hit "q" to exit.'.title())
    print(user)
    
    if user == '':
        #Caliing the function:
        clasify_string(string)

    elif user.lower() == 'q':
    	print(f'=-=-=-=[ exiting the game. come back soon {name}. ]=-=-=-='.title())
    	active = False