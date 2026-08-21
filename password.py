
password = input("ENTER YOUR PASSWORD :")

score = 0

if len(password) >=8:
    print ("LENGTH +8 : ✅")
    score +=1
else:
    print ("LENGTH +8: ❌")

if any(char.isupper() for char in password):
    print ("UPPERCASE: ✅")
    score +=1
else:
    print ("UPPERCASE: ❌")

if any(char.islower() for char in password):
    print ("LOWERCASE: ✅")
    score +=1
else:
    print ("LOWERCASE: ❌")

if any(char.isdigit() for char in password):
    print ("NUMBER: ✅")
    score +=1
else:
    print ("NUMBER: ❌")

if any(char.isalnum() for char in password):
    print ("SYMBOL: ✅")
    score +=1
else:
    print ("SYMBOL: ❌")

print ("score: ",score,"/5")

if score <= 2:
    print ("YOUR PASSWORD IS : WEAK")

elif score <= 4:
    print ("YOUR PASSWORD IS : MEDIUM")

else:
    print ("YOUR PASSWORD IS : STRONG")
