# Calculates the first 8 Mersenne primes (a prime number such that prime_num = 2^p - 1)
# While you can change the number of Mersenne primes the function calculates, anything 
# beyond 8 takes an inordinately long time. While the 8th Mersenne prime is 2,147,483,647,
# (2 ^ 31), the 9th is a whopping 2,305,843,009,213,693,951 (2 ^ 61)

from cryptomath import is_prime

mersennes = []
n = 2
while len(mersennes) < 8:
    num = 2 ** n - 1
    if is_prime(num):
        mersennes.append((n, num)) # n = exponent, num = prime number
    n += 1

print(mersennes)