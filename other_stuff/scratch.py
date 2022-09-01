import time
from cryptomath import is_prime as ip
from cryptomath import calc_primes as cp

a = cp(100000)
for num in a:
    print(f"{num:,}", end=" | ")
print(type(num))