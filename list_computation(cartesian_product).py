''' Compute their Cartesian product, AxB of two lists. Each list has no more than 10 numbers.

For example, given the two input lists:
A = [1,2]
B = [3,4]

then the Cartesian product output should be:
AxB = [(1,3),(1,4),(2,3),(2,4)]
'''

from itertools import product

a = map(int, input('Input list A (separate input values by spaces only): ').split())
b = map(int, input('Input list B (separate input values by spaces only): ').split())

print('AxB =', *product(a, b))
