n, m = 4, 6
word = "abc"
matrix = [
    "raaagg",
    "asdfgg",
    "bxcvgg",
    "cyuigg"
]   

def is_word_in_matrix(word, matrix):
   columns = [[]]
   for i in range(0, n):
        if word in matrix[i]:
            return 'YES'
        elif word[::-1] in matrix[i]:
            return 'YES'
   
   for i in range(0, m):
        column = []
        for j in range(0, n):
            column.append(matrix[j][i])
        columns.append(column)

   for column in columns:
       col = "".join(column)
       if word in col or word[::-1] in col:
           return "YES"
   return "NO"

print(is_word_in_matrix(word, matrix))