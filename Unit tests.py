# FILEPATH: /c:/Users/David/Desktop/PythonPractice/test_single_password_generator.py
import unittest
from single_password_generator import generate_password
import string

class TestPasswordGenerator(unittest.TestCase):
    def test_length_of_password(self):
        length = 10
        password = generate_password(length)
        self.assertEqual(len(password), length)

    def test_contains_only_valid_characters(self):
        length = 20
        password = generate_password(length)
        all_characters = string.ascii_letters + string.digits + string.punctuation
        for char in password:
            self.assertIn(char, all_characters)

    def test_randomness_of_passwords(self):
        length = 15
        password1 = generate_password(length)
        password2 = generate_password(length)
        self.assertNotEqual(password1, password2)

if __name__ == "__main__":
    unittest.main()