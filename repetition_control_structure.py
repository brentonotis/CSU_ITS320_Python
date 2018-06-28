''' Write a program that utilizes a loop to read a set of five floating-point values from user input. 
Ask the user to enter the values, then print the following data:

Total, Average, Maximum, Minimum, Interest at 20% for each original value entered by the user 
(use formula original value = original value + original value * .02)
'''

original_value = [float(x) for x in input('Enter 5 random numbers (seperated by spaces): ').split()]

while len(original_value) != 5:
    original_value = [float(x) for x in input('You did not enter 5 numbers! Try again. Enter 5 random numbers (seperated by spaces): ').split()]
else:
    total_value = sum(original_value)
    average_value = (total_value/len(original_value))
    maximum_value = max(original_value)
    minimum_value = min(original_value)
    interest_value1 = original_value[0] + original_value[0]*.02
    interest_value2 = original_value[1] + original_value[1]*.02
    interest_value3 = original_value[2] + original_value[2]*.02
    interest_value4 = original_value[3] + original_value[3]*.02
    interest_value5 = original_value[4] + original_value[4]*.02

print("The sum is", total_value)
print("The average is", average_value)
print("The maximum value is", maximum_value)
print("The minimum value is", minimum_value)
print("The interest for value 1 is", interest_value1)
print("The interest for value 2 is", interest_value2)
print("The interest for value 3 is", interest_value3)
print("The interest for value 4 is", interest_value4)
print("The interest for value 5 is", interest_value5)
