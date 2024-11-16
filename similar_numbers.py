n = 4
numbers = [107653311, 349562342, 118762293, 840780631]
numbers.sort()

def f():
    for index, num in enumerate(numbers):
        if index + 1 < len(numbers)-1:
            if abs(num - numbers[index+1]) == 1:
                return "YES"
        return "NO"
print(f())