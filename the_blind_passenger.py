import math
t = int(input())

numbers = [int(input()) for _ in range(t)]

def side_and(number):
    t = number % 10
    if t == 2 or t == 1: 
        return "W L"
    elif t == 3 or t == 0:
        return "A L"
    elif t == 4 or t == 9:
        return "A R"
    elif t == 5 or t == 8:
        return "M R"
    elif t == 6 or t == 7:
        return "W R"
    
def row_no(number):
    number -= 1
    d = math.ceil(number / 5)
    return d

for number in numbers:
    if number == 1:
        print("poor conductor")
    else:
        print(f"{row_no(number)} {side_and(number)}")