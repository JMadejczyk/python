n = int(input())
chessboard = [input() for _ in range(n)]

def check_knight_attack_number(i, j, chessboard) -> int:
    summ = 0
    n = len(chessboard)
    if i - 2 >= 0 and j - 1 >= 0:
        if chessboard[i-2][j-1] == "s":
            summ += 1
    
    if i - 1 >= 0 and j - 2 >= 0:
        if chessboard[i-1][j-2] == "s":
            summ += 1

    if i + 1 < n and j - 2 >= 0:
        if chessboard[i+1][j-2] == "s":
            summ += 1
    
    if i + 2 < n and j - 1 >= 0:
        if chessboard[i+2][j-1] == "s":
            summ += 1
    
    if i + 2 < n and j + 1 < n:
        if chessboard[i+2][j+1] == "s":
            summ += 1
    
    if i + 1 < n and j + 2 < n:
        if chessboard[i+1][j+2] == "s":
            summ += 1
    
    if i - 1 >= 0 and j + 2 < n:
        if chessboard[i-1][j+2] == "s":
            summ += 1
    
    if i - 2 >= 0 and j + 1 < n:
        if chessboard[i-2][j+1] == "s":
            summ += 1
    return summ

summ = 0
for i in range(n):
    for j in range(n):
        if chessboard[i][j] == "s":
            summ += check_knight_attack_number(i, j, chessboard)

print(summ)