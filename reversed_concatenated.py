''' Write a Python function that will accept as input three string values from a user. 
The method should return to the user a concatenation of the string values in reverse order. 
The function is to be called from the main method. In the main method, prompt the user for three strings.
'''

def string_prompt():
    prompt = str(input('Enter three strings (separated by spaces): '))
    return prompt

def string_reverse():
    reversed_string = string_prompt()[::-1] # Call string_prompt (input) function, return reversed input
    concatenated_string = ''.join(reversed_string.split()) # Split/join string to concatenate/remove white space between text
    print('The reversed concatenation of your three string values is:', concatenated_string)

string_reverse()

