brackets = input()

open_brackets = []
majonez_kielecki = True

for bracket in brackets:
    if bracket in "{[(":
        open_brackets.append(bracket)
    else:
        if len(open_brackets) == 0:
            majonez_kielecki = False
            break

        last = open_brackets.pop()
        if not ((bracket == ")" and last == '(') or ( bracket == "}" and last == "{") or bracket == "]" and last == "["):
            majonez_kielecki = False
            break
if len(open_brackets) != 0:
    majonez_kielecki = False
print(majonez_kielecki)
