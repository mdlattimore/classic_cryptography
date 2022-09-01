# This currently generates number until it repeats the seed, then
# returns that number along with the period (the number of digits
# the seed repeats).


def run():
    seed = input("Enter a seed number: ")
    num = seed
    idx = 0
    while True:
        next = int(num[idx]) + int(num[-1])
        if next >= 10:  # Non-carrying addition
            next = next - 10
        num = f"{num}{next}"
        idx += 1    
        if len(num) > len(seed) * 2:
            if seed in num[len(seed) + 1:]:
                break
            
    return (num, seed)


if __name__ == "__main__":
    print()
    value = run()
    result = value[0]
    seed = value[1]
    print()
    print(result)
    print()
    period = len(str(result)) - len(seed)
    print(f"The period for the generated number with seed {seed} is {period}.")
    print()