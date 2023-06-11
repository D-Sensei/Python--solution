#Count Vowel
import termcolor

input_string = input(termcolor.colored(("[*] Enter String :"),"green"))

print("[#] loop and conditional")
def count_vowel(string):
    count= 0
    vowel = "aeiouAIEOU"
    for char in string:
        if char in vowel:
            count  += 1
    return count
result= count_vowel(input_string)

print(termcolor.colored(("No. Of Vowels are "+str(result)),"green"))

print("Using sum")
def count_vowel(string):
    vowel = "aeiouAIEOU"
    vowel_count=sum(1 for char in string if char in vowel)
    return vowel_count
result= count_vowel(input_string)
print(termcolor.colored(("No. Of Vowels are "+str(result)),"green"))
