"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is frue.
"""
import math

#! python3

x = int(input("Enter a number: "))
y = str(x)

if x % 8 == 0 and x % 6 == 0:
    print (y + " " + "is a frue")
else:
    print (y + " " + "is not a frue")