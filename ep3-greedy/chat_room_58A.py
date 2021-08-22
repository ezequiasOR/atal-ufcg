s = input()
word = ''

for letter in s:
    if len(word) == 0 and letter == 'h':
        word += 'h'
    elif len(word) == 1 and letter == 'e':
        word += 'e'
    elif (len(word) == 2 or len(word) == 3) and letter == 'l':
        word += 'l'
    elif len(word) == 4 and letter == 'o':
        word += 'o'

if word == 'hello':
    print('YES')
else:
    print('NO')
