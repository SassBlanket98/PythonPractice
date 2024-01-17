import random
import string
def generate_password(length, count):
    passwords = []
    for i in range(count):
        password = "".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
        passwords.append(password)
    return passwords
passwords = generate_password(13, 5)
print(passwords)