n = 3
matrix = [    
    [10, 15, 9],
    [12, 3, 6],
    [20, 1, 17]
]

bests = []
curr = 0
def sum_moves(i, j, curr_sum, matrix):
    curr_sum += matrix[i][j]
    if i == n-1 and j == n-1:
        bests.append(curr_sum)
    if j < n-1:
        sum_moves(i, j+1, curr_sum, matrix)
    if i < n-1:
        sum_moves(i+1, j, curr_sum, matrix)
    
    
sum_moves(0, 0, curr, matrix)
print(max(bests))
