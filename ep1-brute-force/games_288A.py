# A. Games - (https://codeforces.com/problemset/problem/268/A)

n = int(input())
count = 0
colors = []

for i in range(n):
    colors.append(input().split())

for host in colors:
    for guest in colors:
        if host[0] == guest[1]:
            count += 1

print(count)
