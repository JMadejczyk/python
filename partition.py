every_second_sums = []
every_third_sums = []

n = 7
tab = [-1, 1, 3, 2, 4, 5, 0]

every_second = tab[::2]
every_third = tab[::3]

every_second_ = tab[1::2]
every_third_ = tab[1::3]

every_second__ = tab[2::2]
every_third__ = tab[2::3]


print(every_second)
print(every_third)

for i in range(n):
    for j in range(n):
        every_third_sums.append(sum(every_third[i:j+1]))
        every_second_sums.append(sum(every_second[i:j+1]))
for i in range(n):
    for j in range(n):
        every_third_sums.append(sum(every_third_[i:j+1]))
        every_second_sums.append(sum(every_second_[i:j+1]))
for i in range(n):
    for j in range(n):
        every_third_sums.append(sum(every_third__[i:j+1]))
        every_second_sums.append(sum(every_second__[i:j+1]))
      

every_second_sums.sort(reverse=True)
# print(every_second_sums)
every_third_sums.sort(reverse=True)
# print(every_third_sums)

for el in every_second_sums:
    if el in every_third_sums:
        print(el)
        break