# n = int(input())
n = 5

# points = [[int(x) for x in [line for line in input().split()]] for _ in range(0, n)]
points = [
    [-68, -100],
    [91, -46],
    [-48, -50],
    [-91, 81],
    [-10, -62]
]

def calculate_area(px1, py1, px2, py2, px3, py3):
    x1 = px2 - px1
    y1 = py2 - py1
    x2 = px3 - px1 
    y2 = py3 - py1
    return (abs((x1*y2) - (y1*x2)))/2

areas = []

for i in range(0, n):
    for j in range(i+1, n):
       for k in range(j+1, n):
           areas.append(calculate_area(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1]))

while 0 in areas:
    areas.remove(0)

print(min(areas), max(areas))