import random
import string
all_characters = string.ascii_letters + string.digits + string.punctuation
length = int(input("Tell me the length you want your password to be?: "))
password = "".join(random.sample(all_characters, length))
print("Your password, sire:", password)