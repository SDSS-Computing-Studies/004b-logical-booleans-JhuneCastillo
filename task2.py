#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and a perfect cube.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a perfect cube.
xx is only a perfect square.
xx is only a perfect cube.

Example:
Enter a number: 8
8 is only a perfect cube.
"""
import math

x = int(input ("Enter a number: "))
y = math.sqrt(x)
z = x ** 1/3
a = str(x)

if int(y + 0.5 ) ** 2 == x and int(x) ** 1/3 == z:  
    print(a + " is both a perfect square and a perfect cube")
elif int(y + 0.5) ** 2 == x:
    print(a + " only a perfect square")
elif int(x) ** 1/3 == z:
    print(a + " only a perfect cube")
    