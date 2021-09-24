# python2
# https://codeforces.com/problemset/problem/189/A

import sys
sys.setrecursionlimit(10**6)


def f(val):
    if val == 0:
        return 0
    if val < 0:
        return -999999
    if memo[val] == -1:
        memo[val] = max(1+f(val-a), 1+f(val-b), 1+f(val-c))
    return memo[val]


n, a, b, c = map(int, raw_input().split())

memo = [-1 for j in range(4005)]

print f(n)
