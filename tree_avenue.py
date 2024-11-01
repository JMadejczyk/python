N, h = map(int, input().split())
# trees = [tuple(map(int, input().split())) for _ in range(N)]
trees = [[int(i) for i in input().split()] for _ in range(N)]
trees.sort(key=lambda x: x[0])  
count = 0
max_slope = float('-inf')

for distance, height in trees:
    if distance == 0:
        if height > h:
            count += 1
            max_slope = float('inf')
        continue
    slope = (height - h) / distance
    if slope > max_slope:
        count += 1
        max_slope = slope 


print(count)