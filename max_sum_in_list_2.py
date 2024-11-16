max = 0
curr_sum = 0
list = [int(x) for x in input().split()]

for i in range(0, len(list)):
    curr_sum = 0
    for j in range(i, len(list)):
        curr_sum += list[j]
        if curr_sum > max:
            max = curr_sum
print(max)