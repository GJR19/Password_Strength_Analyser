import string

password = "cricket"

#To check if password contains atleast one of these
upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters=[upper_case, lower_case, special, digits]

#To find length of password
length=len(password)
score=0

#Common passwords
with open('10k most common.txt','r') as f:
    common=f.read().splitlines()
if password in common:
    print("Your password is too COMMON!!! SCORE = 0/7")
    exit()

#To find score
if length>8:
    score+=1
if length>12:
    score+=1
if length>17:
    score+=1
if length>20:
    score+=1

print(f"Password length is {str(length)}")
if sum(characters)>1:
    score+=1
if sum(characters)>=2:
    score+=1
if sum(characters)>=3:
    score+=1
print(f"Password has {str(sum(characters))} different character types")

#To find strength of password
if score<5:
    print(f"The password is TOO WEAK !!! SCORE: {str(score)}/7")
elif score==4:
    print(f"The password is MODERATE !!! SCORE: {str(score)}/7")
elif score>4 and score<6:
    print(f"The password is GOOD !!! SCORE: {str(score)}/7")
elif score>6:
    print(f"The password is STRONG !!! SCORE: {str(score)}/7")