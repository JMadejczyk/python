n = int(input())
trees = sorted([int(input()) for _ in range(n)])

def find_minimal_distance(numbers):
    min = float('inf')
    for i in range(len(numbers)-1):
        c = numbers[i+1] - numbers[i]
        if c < min:
            min = c

    return min
min_distance = find_minimal_distance(trees)

def get_distance(a, b):
    return abs(a-b)

do = True
print(min_distance)
while (trees[-1] - trees[0]) % min_distance != 0 or do:
    do = False
    
    for tree in trees:
        if (tree - trees[0]) % min_distance != 0:
            min_distance = max(min_distance - 1, 1)
            break

print(((trees[-1] - trees[0])//min_distance)+1-len(trees))
    

