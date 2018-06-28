''' Write a Python function that will accept as input three string values from a user. 
The method should return to the user a concatenation of the string values in reverse order. 
The function is to be called from the main method. In the main method, prompt the user for three strings.
'''

def string_reverse():
    first_string = str(input('Enter string one: '))
    second_string = str(input('Enter string two: '))
    third_string = str(input('Enter string three: '))
    new_string = first_string + second_string + third_string # Concatenate the three user strings to one
    reversed_string = new_string[::-1] # Reverse the concatenated string
    print('The reversed concatenation of your three string values is:', reversed_string)
   
string_reverse()
    
# Instructor feedback: Prompt not in the main method; There is no main method defined. Missing required main method
