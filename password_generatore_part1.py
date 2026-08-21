import string
import random

n1 = list(string.ascii_lowercase)
n2 = list(string.ascii_uppercase)
n3 = list(string.digits)
n4 = list(string.punctuation)

characters_number = input("Enter Password Length?: ")

while True:
    try:
        characters_number = int(characters_number)
        if characters_number <6:
            print ("please enter six numbers or more digits")
            characters_number = input("please try again enter your password?: ")
        else:
            break
    except:
        print ("please enter your password only")
        characters_number = input("Enter Password Length?: ")
        continue

random.shuffle(n1)
random.shuffle(n2)
random.shuffle(n3)
random.shuffle(n4)

part1 = round(characters_number * (25/100))
part2 = round(characters_number * (25/100))


password = []

for m in range(part1):
    password.append(n1 [m])
    password.append(n2 [m])


for m in range(part1):
    password.append(n3 [m])
    password.append(n4 [m])

random.shuffle(password)

password = "".join(password[0:])

print (password)

