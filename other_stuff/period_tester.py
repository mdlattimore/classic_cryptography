import time
import random



def chained_digit_generator():
    """Chained digit generator. Returns number and seed as strings"""
    print()
    seed = input("Enter a seed number: ")
    num_digits = int(input("How many digits? "))
    start = time.perf_counter()
    num = seed
    idx = 0
    for n in range (num_digits - len(seed)):
        next = int(num[idx]) + int(num[-1])
        if next >= 10:  # non-carrying
            next = next - 10
        num = f"{num}{next}"
        idx += 1
    stop = time.perf_counter()
    print()
    print(f"Time to generate number: {stop - start} seconds.")
    return (num, seed)


# def random_module_generator():
#     """ Generates random number using Python standard library random module. Returns number and seed as strings. For now, you have to hard code the number of digits by manipulating the range."""
#     num = random.randint(10000000000000000000000000000000000000000000000000, 99999999999999999999999999999999999999999999999999)
#     num_str = str(num)
#     seed = num_str[0:5]
#     return (num_str, seed)

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
    seed = number[0:5]
    return (number, seed)



def check(prng_function):
    result = prng_function()  # Substitute with generator of your choice. Generator must return the PR number and initial seed as strings. Prints numbers of less than 1000 digits
    start = time.perf_counter()
    number = result[0]
    seed = result[1]
    adj_number = number[len(seed):]
    search = adj_number.find(seed)
    print()
    if len(number) < 1000:
        print(f"Number: {number}")
    else:
        print(f"Number (truncated): {number[0:100]} ... {number[-100:]}")

    print()
    if search == -1:
        print("No period found")
    else:
        period = search + len(seed)
        print(f"Period: {period}")
    stop = time.perf_counter()
    print()
    print(f"Time to analyze number: {stop - start} seconds.")
    print()
    



if __name__ == "__main__":
    gens = ["Chained Digit Generator", "Random Module Generator"]
    print()
    for key, value in enumerate(gens):
        print(f"{key + 1}: {value}")
    print()
    print("Select generator")
    selection = int(input("> "))
    if selection == 1:
        check(chained_digit_generator)
    elif selection == 2:
        check(random_module_generator)
    
        