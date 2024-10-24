n = 5
mapp = [
    [0,0,1,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [0,1,1,0,0],
    [0,1,1,1,1],
                ]

visited_map = []
for i in range(0, len(mapp)):
    visited_row = []
    for j in range(0, len(mapp[0])):
        visited_row.append(False)
    visited_map.append(visited_row)

island_counter = 0

def check_island(x, y):
    current = mapp[x][y]
    if not visited_map[x][y]:
        visited_map[x][y] = True
        if current == 1:
            # check neighbours
            if x - 1 >= 0:
                check_island(x - 1, y)
            if x + 1 < len(mapp):
                check_island(x + 1, y)
            if y - 1 >= 0:
                check_island(x, y - 1)
            if y + 1 < len(mapp):
                check_island(x, y + 1)

for x in range(0, len(mapp)):
    for y in range(0, len(mapp[0])):
        if mapp[x][y] == 1 and visited_map[x][y] == False:
            check_island(x,y)
            island_counter += 1

print(island_counter)