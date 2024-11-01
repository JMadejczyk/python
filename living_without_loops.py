# n, k = input().split()
# n = int(n)
# k = int(k)
# curr = n
def func(n, k, curr, flag):
    print(curr)
    if curr > 0 and flag == 0:
        func(n, k, curr - k, 0)

    elif curr <= 0 or flag == 1 and curr < n:
        func(n, k, curr + k, 1)

func(10, 7, 10, 0)
