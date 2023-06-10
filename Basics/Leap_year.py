# code for find leap year

import termcolor

year = int(input(termcolor.colored(("[$] Enter number to check even or odd-"),'green')))


def leap_year(year):
    if year%4==0 and( year%100!= 0 or year%400==0) :
        return True
    else:
        return False


if leap_year(year):
    print(termcolor.colored((str(year)+ " is a leap year."),"green"))
else:
    print(termcolor.colored((str(year)+ " is not a leap year."),"green"))
