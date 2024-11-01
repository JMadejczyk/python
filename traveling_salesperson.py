import math
N = int(input())

coords = {}
for _ in range(N):
    city, x, y = input().split()
    coords[city] = {"x": int(x), "y": int(y)}

tour = [x for x in input().split()]
if tour[0] != tour[-1]:
    tour.append(tour[0])

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))

summ = 0
for index, city in enumerate(tour):
    if index < len(tour) - 1:
        summ += calculate_distance(coords[city]["x"], coords[city]["y"], coords[tour[index+1]]["x"], coords[tour[index+1]]["y"])
print(round(summ, 3))
