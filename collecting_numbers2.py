n = int(input())
board = [[int(x) for x in input().split()] for _ in range(n)]

def max_path_sum(board):
    tab = [[0] * n for _ in range(n)]
    tab[0][0] = board[0][0]
    
    for j in range(1, n):
        tab[0][j] = tab[0][j - 1] + board[0][j]
    
    for i in range(1, n):
        tab[i][0] = tab[i - 1][0] + board[i][0]
    
    for i in range(1, n):
        for j in range(1, n):
            tab[i][j] = max(tab[i - 1][j], tab[i][j - 1]) + board[i][j]
    return tab[n - 1][n - 1]

print(max_path_sum(board))
