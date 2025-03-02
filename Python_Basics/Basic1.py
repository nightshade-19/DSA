"""
Following Learn X in Y mins; where x = Python

current time [02-Mar-2025] 6:02AM [P.S. we is not ready for this but we ball]

my mouse and laptop setup is weird now ;-;

THIS WAS A MULTILINE COMMMENT
"""

# DATA-TYPES AND OPERATORS   [We does not like the diffrence in color of the comments :<]

3
print(3)

print(1+1)

print(2-1)

print(1-2)

print(2*3)

print(20/2)

print(2/20)

'''print(20/0) #returs error'''

'''Soo Shift+Enter to run the single line in vs code'''
'''#Floor divvision?? read about it pls '''

1 + 1   # => 2
8 - 1   # => 7
10 * 2  # => 20
35 / 5  # => 7.0

# Floor division rounds towards negative infinity
5 // 3       # => 1
-5 // 3      # => -2
5.0 // 3.0   # => 1.0  # works on floats too
-5.0 // 3.0  # => -2.0

# The result of division is always a float
10.0 / 3  # => 3.3333333333333335

# Modulo operation
7 % 3   # => 1
# i % j have the same sign as j, unlike C
-7 % 3  # => 2   
'''why 2?'''

# Exponentiation (x**y, x to the yth power)
2**3  # => 8

# Enforce precedence with parentheses
1 + 3 * 2    # => 7
(1 + 3) * 2  # => 8

# Boolean values are primitives (Note: the capitalization)
True   # => True
False  # => False

# negate with not
not True   # => False
not False  # => True

# Boolean Operators
# Note "and" and "or" are case-sensitive
True and False  # => False
False or True   # => True

# True and False are actually 1 and 0 but with different keywords
True + True  # => 2
True * 8     # => 8
False - 5    # => -5

# Comparison operators look at the numerical value of True and False
0 == False   # => True
2 > True     # => True
2 == True    # => False
-5 != False  # => True

# None, 0, and empty strings/lists/dicts/tuples/sets all evaluate to False.
# All other values are True
bool(0)      # => False
bool("")     # => False
bool([])     # => False
bool({})     # => False
bool(())     # => False
bool(set())  # => False
bool(4)      # => True
bool(-6)     # => True

# Using boolean logical operators on ints casts them to booleans for evaluation,
# but their non-cast value is returned. Don't mix up with bool(ints) and bitwise
# and/or (&,|)
bool(0)   # => False
bool(2)   # => True
0 and 2   # => 0
bool(-5)  # => True
bool(2)   # => True
-5 or 0   # => -5

# Equality is ==
1 == 1  # => True
2 == 1  # => False

# Inequality is !=
1 != 1  # => False
2 != 1  # => True

# More comparisons
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# Seeing whether a value is in a range
1 < 2 and 2 < 3  # => True
2 < 3 and 3 < 2  # => False
# Chaining makes this look nicer
1 < 2 < 3  # => True
2 < 3 < 2  # => False

# (is vs. ==) is checks if two variables refer to the same object, but == checks
# if the objects pointed to have the same values.
a = [1, 2, 3, 4]  # Point a at a new list, [1, 2, 3, 4]
b = a             # Point b at what a is pointing to
b is a            # => True, a and b refer to the same object
b == a            # => True, a's and b's objects are equal
b = [1, 2, 3, 4]  # Point b at a new list, [1, 2, 3, 4]
b is a            # => False, a and b do not refer to the same object
b == a            # => True, a's and b's objects are equal

#symbols
1 < 2 | 2 < 3
1 < 2 & 2 < 3

'''
it's [02-Mar-2025] 6:43AM we closing for Attempt 1
'''