N, M = [int(x) for x in input().split()]
str0 = input().strip()

formats = []

for line in range(M):
    a, b, c = [x for x in input().split(";")]
    formats.append([a, b, c])

def transform_word(format, str0):
   
    a, b, s = format
    a = int(a)
    b = int(b)

    min_ab = min(a, b)
    max_ab = max(a, b)
    str1 = str0[:min_ab]
    str2 = str0[max_ab+1:]
    return str1 + s + str2

words = [str0]
for format in formats:
    str0 = transform_word(format, str0)
    words.append(str0)
print(str0)

longest_word = ""
for index, word in enumerate(words):
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)