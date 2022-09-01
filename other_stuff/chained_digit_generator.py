"""A (very) pseudorandom number generator. Asks user for seed number and the desired number of digits for the pseudorandom number. Calculates number by adding the first and last digits, appending the digit in the ones place of the result to the end of the number, then repeat by adding the 2nd digit to the last, then the 3rd to the last, and so on, until the desired number of digits is reached. """


def run():
    print()
    seed = input("Enter a seed number: ")
    num_digits = int(input("How many digits? "))
    num = seed
    idx = 0
    for n in range (num_digits - len(seed)):
        next = int(num[idx]) + int(num[-1])
        if next >= 10:  # non-carrying
            next = next - 10
        num = f"{num}{next}"
        idx += 1
    return num  


if __name__ == "__main__":
    result = run()
    print(f"> {result}")  
    print()


