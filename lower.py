# n = int(input())
# tab = [int(x) for x in input().split()]
n = 5
tab = [10, 4, 8, 7, 3]
i = 0

count = 0
def count_moves(tab, j):
    count = 0
    n = len(tab)
    i = 0
    for i in range(j, n-1):
        if tab[i] >= tab[i+1]:
            count += 1
            print(count, *tab)

        else:
            print(count, *tab)
            return count, i+1
        
    return count, i+1

        
while i < len(tab[i:]):
    count_, i = count_moves(tab, i)
    if count_ > count:
        count = count_

print(count)
