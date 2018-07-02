''' Write a Python function that will accept as input three string values from a user. 
The method should return to the user a concatenation of the string values in reverse order. 
The function is to be called from the main method. In the main method, prompt the user for three strings.
'''

def prompt():
    prompt = str(input('Enter three strings (separated by spaces): '))
    return prompt

def main():
    reversed_string = prompt()[::-1]
    concatenated_string = ''.join(reversed_string.split())
    print('The reversed concatenation of your string values is:', concatenated_string)

if __name__ == '__main__':
    main()

main()

'''Corrections per instructor feedback:
      * wrote separate function that will accept three string values
      * defined main method
      * called input function in main method
'''

