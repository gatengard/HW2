numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = {}
for i in numbers:
    if i == 1:
        continue
    for k in range(2, i+2):
        if i == k:
            continue
        if i % k == 0:
            is_prime.update ({i: 'false'})
            break
        else:
            is_prime.update({i: 'true'})
for j, l in is_prime.items():
    if l == 'true':
        primes.append(j)
    else:
        not_primes.append(j)
print(is_prime)
print(primes)
print(not_primes)



