# Cryptomath Module

# The first two functions are from
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

def gcd(a, b):
    # Return greatest common divisor (GCD) of a and b using
    # Euclid's algorithm
    while a != 0:
        a, b = b % a, a
    return b


def find_mod_inverse(a, m):
    # Return the modular inverse of a % m, which is
    # the number x such that (a*x) % m = 1.

    if gcd(a, m) != 1:
        return None  # No mod inverse if a & m are not relatively prime.

    # Calculate usig the extended Euclidean algorithm
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


# My functions
def is_prime(num):
    n = 2
    while n <= num ** .5:
        if num % n == 0:
            return False
        n += 1    
    return True


def calc_primes(n, start=2):
    """List the first 'n' primes from and including 'start'. Default start value is the first prime, 2.""" 
    primes = []
    num = start
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


         
       