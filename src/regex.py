import random
import re
string = 'My number is 415-555-4242.'
# phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
# match_obj = phone_num_pattern_obj.search(string)
# match_obj.group()

# phone_re = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phone_re.search(string)
# print(mo.groups())

# string2 = 'Cell: 415-555-9999 Work: 212-555-0000'
# pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
# searched = pattern.findall(string2)
# print(searched)

# string3 = 'RoboCop eats BABY FOOD.'

# pattern = re.compile(r"[aeiouAEIOU]")

# to_print = pattern.findall(string3)
# print(string3)
# print(to_print)

# pattern1 = re.compile(r'Eggs (and spam+)')
# last_str = pattern1.search('Eggs and spamming')
# print(last_str.group())

# quote =  "My name is Neo. My phone number is 534-342-1234. My email is TheMatrixMan@gmail.com"

# to get the first and last letter of a string. There are two known ways.
## 1 with re library
#  ## using /A or ^ plus the type of character to match as the initial character of the sting. e.g re.findall(/A[A-Za-z], string_to_look_for_pattern)
#  ## Using the matching characters for the last character to get plus the /Z or dollar sign. e.g re.findall([A-Za-z]$) or it could have been replace $ with /Z

## 2 with list properties for strings calling string sub 0 and sub -1
#  ## e.g string = abc   string[0] --> 'a'; string[-1] --> 'c' 



# digits_3 = re.findall(r'',quote)
# digist_str = []
# digist_str.append(quote[0])
# digist_str.append(quote[-1])
# # print(digits_3)
# print(digist_str)



# string = "I like the mountains and the spring"

# string_to_find = re.findall('[a-zA-Z]' , string)
# print(string_to_find)

# string = "I have 123,456 koalas!"

# string_to_find = re.findall('[0-4]' , string)
# print(string_to_find)

# string = "you can see sea shells by the sea shore."

# string_to_find = re.findall('s.a' , string)
# print(string_to_find)

# string = "you can see sea shells by the seaa shore."

# string_to_find = re.findall('s.a{2}' , string)
# print(string_to_find)



# string = "Well well well... if it isn't Will Wilmer"
# string_to_find = re.findall(r'W.{2}l' , string)
# print(string_to_find)

# string = "Happy birthday to you. Happy birhday to you. Happy birthday dear Alex, happy birthday to you."
# string_to_find = re.findall(r"^Happy" , string)
# print(string_to_find)

# * + ? 
## * zero or more
## + one or more
## ? zero or one

# string = "This thing called a Thimble ha Thrice hurt me"
# string_to_find = re.findall(r"Thi.*" , string)
# print(string_to_find)



# random_text = """
# My name is Mr, Neo. My phone nuber is 123-456-7890. My email is ChosenOne@gmail.com
# My name is Mr. Morphius. My phone number is 413-234-2568. My email is ChosenOneGirl@apple.com
# My name is Mrs. Trinity. My phone number is 285-036-8215. My email is ChosenOnesGirl@apple.com.

# """
# pattern = re.compile(r"[\S]+@.+\.\w{2,4}")
# to_print = pattern.findall(random_text)

# print(to_print)

# random_text = """
# My name is Mr, Neo. My phone nuber is (123) 456-7890. My email is ChosenOne@gmail.com
# My name is Mr. Morphius. My phone number is 413 234 2568. My email is ChosenOneGirl@apple.com
# My name is Mrs. Trinity. My phone number is 285-036-8215. My email is ChosenOnesGirl@apple.com.

# """
# pattern = re.compile(r"[\w]+@{1}[\w+\.{1}\w]+")
# to_print = pattern.findall(random_text)

# print(to_print)

# def plain_num(phone):
#     string_list = []
#     for sub_phone in phone:
#         if sub_phone != "(" and sub_phone != ")" and sub_phone != " " and sub_phone != "-":
#             string_list.append(sub_phone)
#     final_string = "".join(string_list)
#     print(final_string)
#     return final_string



# random_text = """
# My name is Mr, Neo. My phone nuber is (123) 456-7890. My email is ChosenOne@gmail.com
# My name is Mr. Morphius. My phone number is 413 234 2568. My email is ChosenOneGirl@apple.com
# My name is Mrs. Trinity. My phone number is 285-036-8215. My email is ChosenOnesGirl@apple.com.

# """
# pattern = re.compile(r"\d{3}[-' '\(\)]+\d{3}[-' '\(\)]+\d{4}")
# to_print = pattern.findall(random_text)
# for string in to_print:
#     string = plain_num(string)


# string_look = " Eggs"
# string_compiled = r"Eggs( and spam)+"
# to_print = re.search("Eggs( and spam)*", string_look)
# print(to_print)


# name_pattern = re.compile(r'First Name: (.*) Last Name: (.*)')
# name_match = name_pattern.search('First Name: Al Last Name: Sweigart')
# var_p = name_match.groups()
# print(var_p)

# no_newline_re = re.compile(r'[A-Za-z.0-9" "\n]*')
# to_print = no_newline_re.search('Serve the public trust. \nProtect the innocent. \nuphold the law.').group()
# print(to_print)


# no_newline_re = re.compile('.*', re.DOTALL)
# to_print = no_newline_re.search('Serve the public trust. \nProtect the innocent. \nuphold the law.').group()
# print(to_print)


# ends_with_number = re.compile(r'\d$')
# print(ends_with_number.search('Your number is 42'))

# print(ends_with_number.search(r'Your number is forty two'))


# pattern  = re.compile(r'\bcat\a*?\b')
# obj_t_print = pattern.findall("The cat found a catapult catalog in the catacombs.")
# print(obj_t_print)


# agent_patter = re.compile(r'(Agent) (\w)\w*')
# print(agent_patter.sub(r"\1******","Agent Alice contacted Agent Bob."))


## Sub basically works the way it is shown above. YOu call the compile vcariable plus .sub(a,b) a is the new string that is going to be used. b is the old string that is going to get replaced
### It is pretty simple. Also, you may have to do more tasks under a substring group. You could call a group by just in a say 1xxx or 1*** or 1 something. It will be calling the results of the group 1 if wsithin the compile variable it was divided by groups

