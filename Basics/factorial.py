#Write a Python program to find the factorial of a number.

import termcolor

num = int(input(termcolor.colored(("[$] Enter number -"),'green')))

print("Using loop")
def factorial_itterative(n):
    factorial=1
    for i in range (1,n+1):
        factorial*=i
    return factorial

result = factorial_itterative(num)


print(termcolor.colored((result),"green"))


print("Using Recursion")

def factorial_recursion(n):
    if n==0:
        return 1
    else:
        return n*factorial_recursion(n-1)
    
result2 = factorial_recursion(num)
print(termcolor.colored((result2),"green"))




print("Using module")
import math

def factorial_module(n):
    return math.factorial(n)
result3 = factorial_module(num)
print(termcolor.colored((result3),"green"))
