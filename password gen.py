import random
import string
from password_strength import psc


def generate_password(length):
    password = ''
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    symbols = string.punctuation
    nums = "0123456789"

    for i in range(length//4):
        password += random.choice(lower)
        password += random.choice(upper)
        password += random.choice(symbols)
        password += random.choice(nums)

    if length%4 == 3:
        password += random.choice(lower)
        password += random.choice(upper)
        password += random.choice(nums)

    elif length%4 == 2:
        password += random.choice(lower)
        password += random.choice(upper)

    elif length%4 == 1:
        password += random.choice(lower)

    return password


length = int(input("Password Length: "))

if length < 4:
    print("Password length should be at least 4")
else: 
    try:
        print(generate_password(length))
        print(psc(generate_password(length)))
    except ZeroDivisionError:
        print("Password length cannot be zero.")