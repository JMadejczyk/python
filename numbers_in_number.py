number = "123123"

def select_n(n: int, string_: str) -> list:
    tab = []
    for i in range(0, len(string_)):
        tab.append(string_[i:n+i])
    tab.reverse()
    tabb = []
    for t in tab:
        if len(t) == n:
            tabb.append(t)
    tabb.reverse()
    return tabb

number_parts = []
for i in range(1, len(number)+1):
    number_parts.append(select_n(i, number))

# print(number_parts)
numbers = {}
for tab in number_parts:
    for number in tab:
        if number not in numbers:
            numbers[number] = 0
        numbers[number] += 1
# print(numbers)



for l in range(1, len(number)+1):
    max_occur = 0
    max_numbers = []
    for number in numbers:
        if len(number) == l:
            if numbers[number] > max_occur:
                max_occur = numbers[number]
                max_numbers = [number]
            elif numbers[number] == max_occur:
                max_numbers.append(number)
    print(min(max_numbers))
