import re

# question:
"""
write a function that uses regex to make sure the password string it is passed is strong
password minimum requirements:
1. must be at least 8 characters long
2. Must contain upper case and lower case within it
3. Also, must have at least one digit

"""

print( "username = J3susmanu3l")

print("insert passwerd:")
password = input()

lower_case_pattern = re.compile(r'[a-z]+')
upper_case_pattern = re.compile(r'[A-Z]+')
digit_case_pattern = re.compile(r'\d+')
while True:    
    lower_case = lower_case_pattern.findall(password)
    upper_case = upper_case_pattern.findall(password)
    digit_case = digit_case_pattern.findall(password)
    password_lenght = len(password)
    if (lower_case == []) or (upper_case == []) or (digit_case == []) or password_lenght < 8:
        print('Password must containt a lowercase character')
        print('Password must containt an uppercase character')
        print('Password must containt a digit from 0 to 9')
        print('Password must contain at least 8 characters')
        print("Enter password again:")
        password = input()
    else:
        break
    break
print('Password is secure')