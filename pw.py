import random
import string

def generate_password(length=12):
    """Generate a random password with uppercase, lowercase, numbers, and special characters."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate and print a random password
password = generate_password()
print("Generated Password:", password)
