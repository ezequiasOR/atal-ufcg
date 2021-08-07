# A. DZY Loves Chessboard - (https://codeforces.com/problemset/problem/445/A)

n, m = map(int, input().split())

chessboard = []

for row in range(n):
    chessboard = list(input())
    for col in range(len(chessboard)):
        if chessboard[col] == '.':
            if (row + col) % 2 == 0:
                chessboard[col] = 'B'
            else:
                chessboard[col] = 'W'
    print(''.join(chessboard))
