# https://codeforces.com/problemset/problem/698/A

n = int(input())
a = list(map(int, input().split()))

dp = [[0, a[0]] if a[0] != 0 else [1, 0]]

for i in range(1, n):
    if a[i] == 0:
        dp.append([dp[-1][0] + 1, a[i]])
    elif a[i] == 3:
        if dp[-1][1] == 1:
            dp.append([dp[-1][0], 2])
        elif dp[-1][1] == 2:
            dp.append([dp[-1][0], 1])
        else:
            dp.append([dp[-1][0], a[i]])
    else:
        if dp[-1][1] == a[i]:
            dp.append([dp[-1][0] + 1, 0])
        else:
            dp.append([dp[-1][0], a[i]])


print(dp[-1][0])
