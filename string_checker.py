''' Write a Python program that performs the following tasks: 
Read from the console an arbitrary string S of length less than 50 characters. 
In the first output line, print True if S has any alphanumeric characters. Otherwise, print False. 
In the second line, print True if S has any alphabetical characters. Otherwise, print False. 
In the third line, print True if S has any digits. Otherwise, print False. 
In the fourth line, print True if S has any lowercase characters. Otherwise, print False. 
In the fifth line, print True if S has any uppercase characters. Otherwise, print False. 
Develop Python code that implements the program requirements.
'''

S = input('Enter a string: ')

if S.isalnum() == True:
    print('True')
else:
    print('False')
    
if S.isalpha() == True:
    print('True')
else:
    print('False')

if S.isdigit() == True:
    print('True')
else:
    print('False')

if S.islower() == True:
    print('True')
else:
    print('False')

if S.isupper() == True:
    print('True')
else:
    print('False')
