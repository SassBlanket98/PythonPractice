import random
import string

def generate_password(length, count):
    passwords = []
    for i in range(count):
        password = "".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
        passwords.append(password)
    return passwords

if __name__ == "__main__":
    length = int(input("Enter the length of the passwords: "))
    count = int(input("Enter the number of passwords to generate: "))
    passwords = generate_password(length, count)
    print("\n".join(passwords))