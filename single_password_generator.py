#!/usr/bin/env python3
import random
import string

print("David's Password Generator")

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.sample(all_characters, length))
    return password

if __name__ == "__main__":
    length = int(input("Tell me the length you want your password to be?: "))
    password = generate_password(length)
    print("Your password, kind sir:")
    print(password)