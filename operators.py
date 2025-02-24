"""
1. Operators
Arithmetic Operators
These operators perform mathematical operations like addition, subtraction, etc.
● + : Addition
● - : Subtraction
● * : Multiplication
● / : Division
● % : Modulus (remainder of division)
● // : Floor division (returns the integer part of the division)
● ** : Exponentiation (raising to a power)
Example:
a = 10
b = 5
print(a + b) # Output: 15
print(a - b) # Output: 5
"""

a=10
b=5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)
print(a+b*b)

"""
Comparison Operators
These operators compare two values and return True or False.
● == : Equal to
● != : Not equal to
● > : Greater than
● < : Less than
● >= : Greater than or equal to
● <= : Less than or equal to
"""


x = 10
y = 5

print("Equal to:", x == y)        # False
print("Not equal to:", x != y)    # True
print("Greater than:", x > y)     # True
print("Less than:", x < y)        # False
print("Greater than or equal to:", x >= y)  # True
print("Less than or equal to:", x <= y)  # False


"""
Logical Operators
These operators are used to combine conditional statements.
● and : Returns True if both conditions are true
● or : Returns True if at least one condition is true
● not : Reverses the result (returns True if the condition is false)
"""

x = 10
y = 5

# and operator: True if both conditions are True
print("x > 5 and y > 2:", x > 5 and y > 2)  # True

# or operator: True if at least one condition is True
print("x > 15 or y > 2:", x > 15 or y > 2)  # True

# not operator: Reverses the result
print("not(x > 5):", not(x > 5))  # False


