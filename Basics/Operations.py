# Create a code to take 2 inputs and perform operation (+ - * /) on them

import termcolor
# I used termcolor function to have a colored ouput. You can skip this part.

first_number = int(input(termcolor.colored(("[$] Enter 1st number -"),'green')))
second_number = int(input(termcolor.colored(("[$] Enter 2nd number -"),'green')))
operation = input(termcolor.colored(("[$] Enter operation (+,-,*,/)-"),'green'))


if operation == "+":
    print("[+] The Answer is " + str(first_number + second_number))
elif operation =="-":
    print("[-] The Answer is " + str(first_number - second_number))
elif operation =="*":
    print("[*] The Answer is " + str(first_number * second_number))
elif operation =="*":
    print("[/] The Answer is " + str(first_number / second_number))
else:
    print("[!] Operation doesn't exist ")
