
names = open('Names.txt'.lower(), 'r', encoding="utf8")
readname = names.read().splitlines()


def length(password):
    if len(password) < 8:
        print('🟥 the length of the password should be not be less than 8 characters')
    elif len(password) > 16:
        print('🟥 the length of the password should not be larget than 16 characters')
    else:
        return 'Y'

def digit(password):
    if not any(character.isdigit() for character in password):
        print('🟥 the password should contain atleast one digit')
    else:
        return 'Y'

def upper(password):
    if not any(character.isupper() for character in password):
        print('🟥 the password should contain upper case letters')
    else:
        return 'Y'

def lower(password):
    if not any(character.islower() for character in password):
        print('🟥 the password should contain lower case letters')
    else:
        return 'Y'


def special_chars(password):
    list_ofchars = ["!", "@", "#", "$", "%", "^", "&", "*", "(",")","-","+"]
    if not any(character in list_ofchars for character in password):
        print('🟥 the password should contain atleast one special character')
    else:
        return 'Y'

def similarity(username, password):
    if(username.lower() in password.lower()):
        print('🟥 the password contains similarity to the username')
    else:
        return 'Y'

def palindrome(password):
    for i in range(0, int(len(password)/2)):
        if password[i] != password[len(password)-i-1]:
            return False
        return True

def findname(password):
    for name in readname:
        if name.lower() in password.lower():
            print('🟥 the password contains a name')
            break
    else:
        return 'Y'




def feedback(username, password):

    V_length = length(password)
    V_Digit = digit(password)
    V_Upper = upper(password)
    V_Lower = lower(password)
    V_SpecialC = special_chars(password)
    V_Similarity = similarity(username, password)
    V_name = findname(password)
    




    Score = 0
    if V_length and V_Digit and V_Upper and V_Lower and V_SpecialC and V_Similarity and V_name   == 'Y':
        Score = +10



    if V_SpecialC != 'Y':
        Score = +2

    if V_name != 'Y':
        Score = +2

    if V_Similarity != 'Y':
        Score = +2



    if V_length != 'Y':
        Score = +1

    if V_Lower != 'Y':
        Score = +1

    if V_Upper != 'Y':
        Score = +1

    if V_Digit != 'Y':
        Score = +1


    if Score == 1:
        ans = '🟥 Your password is weak'
        pass
    if Score == 2:
        ans = '🟨 Your password is medium strength'
        pass    
    if Score == 10:
        ans = '🟩 Your Password is strong'
        pass 

    return ans