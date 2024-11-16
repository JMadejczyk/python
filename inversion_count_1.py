n = int(input())
tab = [int(input()) for _ in range(n)]

number = 0
for i in range(n):
    for j in range(n):
        if i < j and tab[i] > tab[j]:
            number += 1