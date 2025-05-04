"""
Till now, we have been working with hardcoded data values.
In real life, we often have to take some input from the user.

Input statement in python allows users to provide data to your program using the terminal
Let us see how it works
"""

"""
Suppose we want to take the name of a user.
"""

name = input("Please enter your name: ")
print(name)

"""
Suppose now we want to take the age of the user
"""

age = input("Please enter your age: ")
print(age)

# Trick question: what is the data type of the age variable.

"""
The input statement by default, converts everything into a string. We have to convert the type
to the right one. You can do it like below by wrapping it in the type
"""

string_age = input("Please enter your age: ")
age = int(string_age)
print(age)


"""
Activity:

Create a python file user_input.py
Get the user's first name, last name, age and phone number. 
Print all these values.
"""