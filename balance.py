n = int(input())
tab = [int(x) for x in input().split()]

total_sum = sum(tab)
left = 0
minimum = float("inf")

for i in range(n - 1):
    left += tab[i]
    right = total_sum - left
    diff = abs(left - right)
    if diff < minimum:
        minimum = diff

print(minimum)