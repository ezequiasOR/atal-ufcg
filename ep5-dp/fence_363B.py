# https://codeforces.com/contest/363/problem/B

n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [99999999999, sum(h[:k])]

for i in range(1, n-k+1):
    dp.append(dp[-1] - h[i-1] + h[i+k-1])

print(dp.index(min(dp)))
