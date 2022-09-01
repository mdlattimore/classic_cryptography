def middle_square():
    print()
    number = ""
    print("Enter seed: ")
    seed = int(input("> "))
    print("How many digits?")
    num_digits = int(input("> "))
    num = seed
    print(type(num))
    print(type(seed))
    for n in range(num_digits):
        sq_num1 = num ** 2
        sq_num = str(sq_num1)
        middle = len(sq_num) // 2
        mid_num = sq_num[middle - 2: middle + 2]
        number += mid_num
        num = int(mid_num)
    return (num, str(seed))

middle_square()