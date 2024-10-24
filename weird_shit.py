numbers = input().split()

def recurrent_s(s, numbers):
    if numbers:
        number = int(numbers.pop())
        s += number
        return recurrent_s(s, numbers)
    else:
        return s
