import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Generate a random string of length 10
random_string = generate_random_string(10)
print("Random String:", random_string)

# Generate another random string of length 15
random_string_15 = generate_random_string(15)
print("Random String (15 characters):", random_string_15)
