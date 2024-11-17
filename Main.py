# Function importing from Functions file

from Functions import palindrome, feedback

# intake

username = input('Enter Your Username: ')
password = input('Enter Your Password: ')

# Testing Functions & returns


print(feedback(username, password))

V_Palindrome = palindrome(password)
    
if (V_Palindrome):
    print('Your password failed the palindrome test ❌')
else:
    print('Your password passed the palindrome test ✔️')
