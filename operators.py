"""
Operators are things you can do with data of different types.
Since variables are pointers to data, operators can be applied to both variables and data.
Let us see some examples.
"""

"""
Assignment Operator (=)

Assignment operator we have seen before, where we assign the value on the right
to the value on the left.
"""
a = 30
print(a)

b = a
print(b)

"""
Activity:

Create a python file name operators.py
Create two variables, num_1 and num_2, and assign them numbers 10 and 20 respectively.
Write the code, using a third variable num_3, to swap their values.
print the old variables and new variable values.
"""


"""
Arithmitic Operator (+, /, -, *, **, %)

Arithmitic operators work with numbers, both integers and floating.
Let us see some examples.
"""
number_1 = 10
number_2 = 10
number_3 = 10+10

print(number_3)
print(number_1 * number_2)
print(10/10)

"""
Activity:
Use the same operators.py file.
Create two number variables, number_1 and number_2. They can be either integers or floating points
Apply all the arithmitic operators that are shown above and see what happens.
"""

"""
Arithmitic Operator Special case: Strings (+, *)

Some of the arithmitic operators work with strings. Let us take some examples

+ means concatenation.
* means reptition
"""

first_name = "Madhav"
space = " "
last_name = "Malhotra"

print(first_name + space + last_name)
print(first_name*10)

"""
Activity:

Use the same operators.py python file
Create two string variables and practice the the two string operators with them.
"""

"""
Comparison operators (==, !=, >, <. >=, <=)
comparison operators well, compare variables

All operators can be used with numbers
==, != is the only one that can also be used with other data types
"""

a = 10
b = 20

result = a<b

print(result)
# Trick question: What is the data type of the result variable?

print(a == b)
# No longer a trick question: What is the data type of the result variable?

"""
Activity:
Use the same operators.py python file
Create two string variables and print if they are equal.
Create two integer variables and print if they are not equal.
Create two integer variables and print results of applying <,>,<=,>= operators on them
"""
