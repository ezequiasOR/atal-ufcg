# A. Common Subsequence - (https://codeforces.com/problemset/problem/1382/A)

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    g = False
    for i in range(n):
        if a[i] in b:
            print('YES')
            print(1, a[i])
            g = True
            break
    if g == False:
        print('NO')
