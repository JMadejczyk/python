# n, m = map(int, input().split()) 
# matrix = [list(map(int, input().split())) for _ in range(n)]
n, m = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(n)]

def max_diagonal_sum(matrix, n, m):
    diag1 = {}  
    diag2 = {}  
    # sums and distinctions of diagonal indexes are the same!
    for i in range(n):
        for j in range(m):
            if (i - j) not in diag1:
                diag1[i - j] = 0
            diag1[i - j] += matrix[i][j]
            
            if (i + j) not in diag2:
                diag2[i + j] = 0
            diag2[i + j] += matrix[i][j]

    return max(max(diag1.values()), max(diag2.values()))

print(max_diagonal_sum(matrix, n, m))



