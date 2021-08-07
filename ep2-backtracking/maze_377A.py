# A. Maze - (https://codeforces.com/problemset/problem/377/A)

def addWalls(row, col):
    count = 0

    queue = [(row,col)]
    cellsChecked[row][col] = True

    while queue:
        coordinate = queue.pop(0)
        count += 1

        y = coordinate[0]
        x = coordinate[1]
        if count > emptyCells-k:
            grid[y][x] = 'X'
 
        if y+1 < n and grid[y+1][x] != '#' and not cellsChecked[y+1][x]:
            queue.append((y+1, x))
            cellsChecked[y+1][x] = True

        if y-1 >= 0 and grid[y-1][x] != '#' and not cellsChecked[y-1][x]:
            queue.append((y-1, x))
            cellsChecked[y-1][x] = True

        if x+1 < m and grid[y][x+1] != '#' and not cellsChecked[y][x+1]:
            queue.append((y, x+1))
            cellsChecked[y][x+1] = True

        if x-1 >= 0 and grid[y][x-1] != '#' and not cellsChecked[y][x-1]:
            queue.append((y, x-1))
            cellsChecked[y][x-1] = True


n, m, k =  map(int,input().split())

cellsChecked = [[False for _ in range(m)] for _ in range(n)]
grid = []
emptyCells = 0
 
for row in range(n):
    line = list(input())
    grid.append(line)
    emptyCells += line.count('.')
    if '.' in line:
        position = (row, line.index('.'))

addWalls(position[0], position[1])

for line in grid:
    print(''.join(line))
