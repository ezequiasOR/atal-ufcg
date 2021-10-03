r, c = map(int, input().split())

forest = []
for _ in range(r):
    line = input()
    forest.append(line)

queue = []
flag = False
vis = [[False for _ in range(c)] for _ in range(r)]

for i in range(r):
    for j in range(c):
        if forest[i][j] == 'E':
            queue.append((i, j))
            vis[i][j] = True
            break

x = [-1, 0, 1, 0]
y = [0, -1, 0, 1]
res = 0

while queue:
    queue2 = []

    while queue:
        i, j = queue.pop(0)

        for k in range(4):
            idxI, idxJ = i + x[k], j + y[k]

            if 0 <= idxJ < c and 0 <= idxI < r and not vis[idxI][idxJ] and forest[idxI][idxJ] != 'T':
                queue2.append((idxI, idxJ))
                vis[idxI][idxJ] = True
                if forest[idxI][idxJ] == 'S':
                    flag = True

                try:
                    res += int(forest[idxI][idxJ])
                except:
                    continue

    if not flag:
        queue = queue2

print(res)
