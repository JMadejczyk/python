# s = input().lower()
s = "aa"

possible_permutations = [s]

for i in range(0, len(s)):
    word = (s[:i] + s[i+1:])
    # print(word)
    if word not in possible_permutations:
        possible_permutations.append(word)

for i in range(0, len(s)):
        word_tab = [x for x in s]
        if word_tab:
            word_tab.pop(i)
        for j in range(0, len(word_tab)):
            # print(word_tab)
            word_tab_copy = word_tab[:]
            if word_tab:
                word_tab_copy.pop(j)
            word = "".join(word_tab_copy)
            # print(word)
            if word not in possible_permutations:
                possible_permutations.append(word)

print(possible_permutations)

def find():
    for word in possible_permutations:
        if word == word[::-1]:
            # print(word[::-1])
            return "YES"
    return "NO"

print(find())
        