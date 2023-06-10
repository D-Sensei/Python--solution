# Write a Python program to find the largest among three numbers.

import termcolor
#OPTIONAL

number = int(input(termcolor.colored(("[$] Enter number to check even or odd-"),'green')))

# Using the Modulo Operator
if number % 2 ==0:
    print(termcolor.colored(("[#] Even"),'green'))
else:
    print(termcolor.colored(("[#] Odd"),'green'))


# Using bitwise AND operator 
if number and 1 == 0:
    print(termcolor.colored(("[#] Even"),'green'))
else:
    print(termcolor.colored(("[#] Odd"),'green'))
