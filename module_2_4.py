numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for n in numbers:
    if n == 1:
        # print(n, '- не является ни простым, ни составным числом')
        continue

    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(n)
    else:
        not_primes.append(n)

print("Primes:", primes)
print("Not Primes:", not_primes)