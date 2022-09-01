from functools import cache

@cache
def fibonacci_of(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)

for x in range(100):
    print(f"{fibonacci_of(x):,}")