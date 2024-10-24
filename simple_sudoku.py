matrix = [[int(x) for x in input().split().strip()] for _ in range(9)]

templete = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def chech():
    for row in matrix:
        if [*sorted(row)] != [*templete]:
            return False
        
    for j in range(9):
        col = []
        for i in range(9):
            col.append(matrix[i][j])

        if [*sorted(col)] != [*templete]:
            return False
    return True

def checkRepublic():
    diagon = []
    for i in range(9):
        diagon.append(matrix[i][i])
    if [*sorted(diagon)] != [*templete]:
        return False
    
    diagon = []
    for i in range(9):
        diagon.append(matrix[i][8-i])
    if [*sorted(diagon)] != [*templete]:
        return False
    
    return True
    
if chech() and checkRepublic():
    print("X")
elif chech():
    print("True")
else:
    print("False")
                
