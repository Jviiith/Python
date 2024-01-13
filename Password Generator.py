# A Python module is a file that contains a set of statements and definitions that you can use in your code.
# In this project, you'll learn how to import modules from the Python standard library. 
# You'll also learn how to use Regular Expressions by building your own password generator program.
# A Python module is a file containing code designed to perform specific tasks. The Python standard library contains many modules that you can import and use in your code. You can achieve this by using the import statement followed by the name of the module.
import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password
 #  In this way, your code won't run when imported as a module. Otherwise, it will call generate_password() and print the generated password.  
if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)
