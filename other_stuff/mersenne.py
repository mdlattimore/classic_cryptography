from cryptomath import is_prime

mersennes = []
n = 2
while len(mersennes) < 8:
    num = 2 ** n - 1
    if is_prime(num):
        mersennes.append((n, num))
    n += 1

print(mersennes)