def solve(n, a):
    pos = [0]
    distances = [-1] * n
    distances[0] = 0

    for p in pos:
        for value in [p - 1, p + 1, a[p] - 1]:
            if value >= 0 and value < n and distances[value] == -1:
                distances[value] = distances[p] + 1
                pos.append(value)

    return distances


n = int(input())
a = list(map(int, input().split()))

res = solve(n, a)

print(*res)
