import termcolor


input_word = input(termcolor.colored(("[*] Enter Number :"),"green"))

print("[#] Using Slice operator")
def palindrome(word):
    if word == word[::-1]:
        print(termcolor.colored(("Yes, its an palindrome"),"green"))
    else:
        print(termcolor.colored(("Not"),"green"))
result = palindrome(input_word)


print("[#] recursion")
def palindrome_recursive(word):
    if len(word)==1:
        return True
    if word[0]!=word[-1]:
        return False
    return palindrome_recursive(word[1:-1]) 

if palindrome_recursive(input_word):
    print(termcolor.colored(("Yes, its an palindrome"),"green"))
else:
    print(termcolor.colored(("Not"),"green"))

