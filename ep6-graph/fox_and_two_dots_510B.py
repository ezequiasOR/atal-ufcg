import Queue
import sys
sys.setrecursionlimit(10**5)

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def valid(row, column):
    if(row >= 0 and row < n and column >= 0 and column < m):
        return True
    return False


def solve(i, j):
    bfs = Queue.Queue()
    bfs.put(((i, j), (-1, -1)))

    while not bfs.empty():
        actual = bfs.get()

        r = actual[0][0]
        c = actual[0][1]

        rCalledBy = actual[1][0]
        cCalledBy = actual[1][1]

        if vis[r][c]:
            return True
        vis[r][c] = True

        for i in xrange(4):
            newR = r + dr[i]
            newC = c + dc[i]

            if(newR == rCalledBy and newC == cCalledBy):
                continue
            if(valid(newR, newC)):
                if(grid[newR][newC] == grid[r][c]):
                    bfs.put(((newR, newC), (r, c)))

    return False


n, m = map(int, raw_input().split())
grid = []

MAXN = 53
vis = []

for i in xrange(MAXN):
    newList = []
    for j in xrange(MAXN):
        newList.append(False)
    vis.append(newList)

for i in xrange(n):
    row = raw_input()
    grid.append(row)

ciclo = 'No'
for i in xrange(n):
    for j in xrange(m):
        if not vis[i][j]:
            if solve(i, j):
                ciclo = 'Yes'
                break

print ciclo
