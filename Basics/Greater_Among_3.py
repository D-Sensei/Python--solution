

import termcolor
#Optional

a = int(input(termcolor.colored(("[$] Enter 1st number -"),'green'))) 
b = int(input(termcolor.colored(("[$] Enter 2nd number -"),'green')))
c = int(input(termcolor.colored(("[$] Enter 3rd number-"),'green')))

# Without termcolor function the above code line would look like 
# int(input("enter value"))

#1st method using elif
if a>b & a>c:
    print("largest number is" , a)
elif b>a & b>c:
    print("largest number is ", b) 
else:
    print("largest number is ", c) 


#2nd mrthod using max function
print("#Using max function")
big_number = max(a,b,c)
print(big_number)
