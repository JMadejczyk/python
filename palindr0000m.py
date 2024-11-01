number = "10100"
n = len(number)
substrings = []

for i in range(n):
    for j in range(i+1, n+1):
        substrings.append(number[i:j])

def is_palindrome(number:str) -> bool:
    number = number.rstrip("0")
    if number == "":
        return False
    tab = [x for x in number]
    if tab == list(reversed(tab)):
        return True
    return False

counter = 0
for number in substrings:
    if is_palindrome(number):
        counter += 1

print(counter)