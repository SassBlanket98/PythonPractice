import random
import string

def generate_password():
    letters = string.ascii_letters
    numbers = string.digits
    special_chars = string.punctuation

    password = random.choices(letters, k=10) + random.choices(numbers, k=3) + random.choices(special_chars, k=5)
    random.shuffle(password)
    password = ''.join(password)

    return password

generated_password = generate_password()
print(generated_password)