'''Write a program that utilizes a loop to read a set of five floating-point values from user input. 
Ask the user to enter the values, then print the following data:

Total Average Maximum Minimum Interest at 20% for each original value entered by the user. 
Use the formula: Interest_Value = Original_value + Original_value*0.2
'''

original_value = [float(x) for x in input('Enter 5 random numbers (seperated by spaces): ').split()]

for i in original_value:
    total_value = sum(original_value)
    average_value = (total_value / len(original_value))
    maximum_value = max(original_value)
    minimum_value = min(original_value)
    interest_value = original_value + original_value*2
    print(total_value, average_value, maximum_value, minimum_value, interest_value)
