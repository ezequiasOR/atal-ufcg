def dfs(num):
    aux[num] = 1
    for j in range(1, n):
        if aux[j] != 1 and (x[num] == x[j] or y[num] == y[j]):
            dfs(j)


n = int(raw_input())+1
x = [0]
y = [0]
aux = [0]*n
resp = 0

for i in range(1, n):
    a, b = map(int, raw_input().split())
    x.append(a)
    y.append(b)

for i in range(1, n):
    if aux[i] != 1:
        dfs(i)
        resp += 1

print resp - 1
