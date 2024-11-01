n = 3
matrix = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
]

ones_list = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            ones_list.append([i+1, j+1])

def calculate_distance(ent1, ent2):
    i1, j1 = ent1
    i2, j2 = ent2
    if i2 % i1 == 0 and j2 % j1 == 0:
        return (abs(i1 - i2) + abs(j1 - j2))
    else:
        return 1000
    
min_distance = 1000
for index, entity in enumerate(ones_list):
    for index2, entity2 in enumerate(ones_list):
        if index != index2:
            distance = calculate_distance(ent1=entity, ent2=entity2)
            if distance < min_distance:
                min_distance = distance

print(min_distance)