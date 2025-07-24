#importing random and string
import random


def generating_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    length = random.randint(8,16)
    password = ""
    password += random.choice(characters)
    return password
print("password :",generating_password)