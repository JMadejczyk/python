n = int(input())
matrix = [[int(x) for x in input().split(" ")] for _ in range(n)]

def matrix_sum(matrix):
    summary = 0
    for x in range(len(matrix)+1):
        for y in range(len(matrix)+1):
            summary += matrix[x][y]
    return summary

maximum = 0
for a in range(0, n+1):
    for b in range(0, n+1):
        for c in range(0, n+1):
            for d in range(0, n+1):
                msum = matrix_sum([x[c:d+1] for x in matrix[a:b+1]])
                if msum > maximum:
                    maximum = msum
print(maximum)
                
