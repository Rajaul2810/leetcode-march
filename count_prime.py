# def count_prime(n):
#     for i in range(2,n+1):
#        for j in range(2,i):
#            if (i % j) == 0:
#                break
#            else:
#                print(i, 'prime')
#
# count_prime(10)
def countPrime(n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
             primes[i * i: n: i] = [False] * len(primes[i * i: n: i])

    return sum(primes)
print(countPrime(10))