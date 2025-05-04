"""
We discussed how python interpretor is executing the statements from top to bottom.
Sometimes, we want to control the flow of that execution. That is where control structures
come into the picture. Let us look at it case by case
"""

"""
Let us say we want to run a piece of code only when a condition is true.
Well, we can do that we conditionals. Let us look at an example.
"""

a = 10
b = 20

if a<b:
    print("hello world")
"""
Here, the indentation is super important. It is what tells python that the block of code is inside
the conditional statement.

The ":" after the if statement is what tells the interpretor, okay, related code block is coming!!!!

Let us look at some other variations of conditionals
"""

"""
What if there are multiple conditions that we want to do. We can do multiple conditional blocks
"""

a = 20
b = 10

if a<b:
    print("Less than")
if a>b:
    print("More than")
if a == b:
    print("Equal")

"""
In the above case, we saw that we can write multiple conditional statements.
Having said that, the interpretor is gonna run all the three if statements even if
it has already found the right one. That is where elif comes into picture
"""

if a<b:
    print("Less than")
elif a>b:
    print("More than")
elif a == b:
    print("Equal")

"""
In the above case, as soon as the first statement is true, the remaining ones will be skipped.
This is an optimization of the code and preventing interpretor from running code it does not need to.
"""

"""
Activity:

Create a python file control_structres.py
Create two number variables, num_1 and num_2 and assign them random values.
Create a third number variable, num_3 and assign it a value.
Using conditionals, print the number with which num 3 is equal to. 
    print "1" if num_3 is equal to number 1
    print "2" if num_3 is equal to number 2 
    check your code works with different values of number 1, number 2 and number 3.

This is not an easy exercise, so take your time. 
"""
num_1 = 20
num_2 = 10
num_3 = 20

if num_3 == num_1:
    print("1")

if num_3 == num_2:
    print("2")


"""
Let us look at another structure: conditional loop.

Suppose you want to continuously run a piece of code until a condition becomes fales.
You can use while loop for this.
"""

a = 0

while a<10:
    print(a)
    a = a+1


"""
Activity:

Use the same python file control_structures.py
Write the code opposite to above. It should print a starting from 10, 
counting down until it is equal to 0.
"""