import math
def generate_primes(n: int) -> list:
    primes = ["2"]
    for i in range(3, n):
        is_prime = True
        for j in range(2, round(math.sqrt(i))+1):
            if i % j == 0:
                is_prime = False
        if is_prime:
            primes.append(str(i))
    return primes

n = "1023"

primes = generate_primes(int(n))

ans = []
for prime in primes:
    if prime in n:
        ans.append(prime)

ans.sort(reverse=True)
for a in ans:
    print(a)