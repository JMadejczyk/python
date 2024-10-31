board = [input() for _ in range(8)]

unsafe = [[0 for _ in range(8)] for _ in range(8)]

def set_col_unsafe(unsafe, col):
    for i in range(8):
        unsafe[i][col] = 1
    return unsafe

def set_row_unsafe(unsafe, row):
    unsafe[row] = [1 for _ in range(8)]
    return unsafe

for i, line in enumerate(board):
    for j, entity in enumerate(line):
        if entity == 'w':
            unsafe = set_row_unsafe(unsafe, i)
            unsafe = set_col_unsafe(unsafe, j)
            unsafe[i][j] = 0


def check_if_under_attack(unsafe, i, j):
    if unsafe[i][j] == 1:
        return True
    else:
        return False

def can_king_move(unsafe, i, j):
    if i - 1 > 0:
        if unsafe[i-1][j] == 0:
            return True    
    if i + 1 < 8:
        if unsafe[i+1][j] == 0:
            return True
    if j - 1 > 0:
        if unsafe[i][j-1] == 0:
            return True 
    if j + 1 < 8:
        if unsafe[i][j+1] == 0:
            return True
    if i - 1 > 0 and j - 1 > 0:
        if unsafe[i-1][j-1] == 0:
            return True
    if i - 1 > 0 and j + 1 < 8:
            if unsafe[i-1][j+1] == 0:
                return True
    if i + 1 < 8 and j - 1 > 0:
        if unsafe[i+1][j-1] == 0:
            return True
    if i + 1 < 8 and j + 1 < 8:
        if unsafe[i+1][j+1] == 0:
            return True
    return False
    

for i, line in enumerate(board):
    for j, entity in enumerate(line):
        if entity == 'k':
            under_attack = check_if_under_attack(unsafe, i, j)
            king_can_move = can_king_move(unsafe, i, j)
            break
if under_attack and not king_can_move:
    print("mat")
elif not under_attack and not king_can_move:
    print("pat")
elif king_can_move:
    print("game goes on")