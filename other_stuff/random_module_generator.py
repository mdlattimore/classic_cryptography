import random

def random_module_generator():
    """ Generates random number using Python standard library random module. Returns number and seed as strings."""
    number = ""
    print()
    print("How many digits? ")
    num_digits = int(input("> "))
    number += str(random.randint(1, 9))  # First number generated from range(1, 9) to prevent leading 0.
    for n in range(num_digits - 1):
        rand_num = random.randint(0, 9)
        number += str(rand_num)
    return number

if __name__ == '__main__':
    print(random_module_generator())