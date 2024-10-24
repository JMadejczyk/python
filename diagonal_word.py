n = 4

strings = [
"sklr",
"yvmc",
"pjnb",
"pbwl"
]

for string in strings:
    for s_index, s in enumerate(string):
        if s == strings[s_index][s_index]:
            print(string)