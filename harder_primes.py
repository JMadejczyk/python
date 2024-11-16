import math
n = int(input())
tab = [int(input()) for _ in range(n)]

def is_prime(n: int) -> bool:

    for j in range(2, round(math.sqrt(n))+1):
        if n % j == 0:
            return False
    return True

for n in tab:
    if is_prime(n) and n>=2:
        print("YES")
    else:
        print("NO")