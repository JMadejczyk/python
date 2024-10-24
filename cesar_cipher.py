n = int(input())
word = input().strip()

lower_tab = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k","l", "m","n","o","p","q","r","s","t","u","v","w","x","y","z" ]
upper_tab = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K","L", "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z" ]

def move(letter, move_by):
    if letter.islower():
        index = lower_tab.index(letter)
        if index - move_by >= 0:
            return lower_tab[index - move_by]
        else: 
            return lower_tab[index - move_by + len(lower_tab)]
    else:
        index = upper_tab.index(letter)
        if index + move_by >= 0:
            return upper_tab[index - move_by]
        else: 
            return upper_tab[index - move_by + len(upper_tab)]
        

for w in word:
    print(move(w, n), end='')