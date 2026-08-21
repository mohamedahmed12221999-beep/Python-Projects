import string
import secrets

chars_num = input("Enter Your Characters?: ")

while True:
    try:
        chars_num = int(chars_num)

        if chars_num < 8:
            print ("The Number You Entered Is Invalid:\n")
            chars_num = input("Please Enter A Characters Eight Or More Digits?: ")
        else:
            break
    except ValueError:
        chars_num = input(" Enter A Charcters Only: ")
        continue


n1 = list(string.ascii_lowercase)
n2 = list(string.ascii_uppercase)
n3 = list(string.digits)
n4 = list(string.punctuation)


all_chars = n1 + n2 + n3 + n4
password = []

password.append(secrets.choice(n1))
password.append(secrets.choice(n2))
password.append(secrets.choice(n3))
password.append(secrets.choice(n4))

for m in range(chars_num - 4):
    password.append(secrets.choice(all_chars))
secrets.SystemRandom().shuffle(password)

password = "".join(password)

print (f"Your Password Is:\n     ⬇    \n     ⬇    \n     ⬇    \n{password}\n")
