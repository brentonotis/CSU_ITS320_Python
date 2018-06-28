'''Implement a program that reads in a year and outputs the approximate value of a Ferrari 250 GTO in that year. 
Use the following table that describes the estimated value of a GTO at different times since 1962. Prompt input for value.

1962-1964: $18,500 
1965-1968: $6,000 
1969-1971: $12,000 
1972-1975: $48,000 
1976-1980: $200,000 
1981-1985: $650,000 
1986-2012: $35,000,000 
2013-2014: $52,000,000
'''

GTO_year = int(input("Congratulations, you own a Ferrari 250 GTO! Enter any year between 1962 and 2014 to determine the estimated value of your GTO at that time: "))
value = int()

if GTO_year <= 1964 and GTO_year >= 1962:
    value = 18500
elif GTO_year <= 1968:
    value = 6000
elif GTO_year <= 1971:
    value = 1200
elif GTO_year <= 1975:
    value = 48000
elif GTO_year <= 1980:
    value = 200000
elif GTO_year <= 1985:
    value = 650000
elif GTO_year <= 2012:
    value = 35000000
elif GTO_year <= 2014:
    value = 52000000
else:
    value = "Gazillion...Not really...Please enter a year between 1962 - 2014 for the program to function as intended."
print("The value of your GTO in ", GTO_year, " was $", value, sep = '')
