# python2
# https://codeforces.com/contest/727/problem/A

from collections import deque
a, b = map(int, raw_input().split())
pre = {}
fila = deque([a])

while fila:
    value = fila.popleft()
    d = 2 * value
    if d not in pre and d <= b:
        fila.append(d)
        pre[d] = value
    n = 10 * value + 1
    if n not in pre and n <= b:
        fila.append(n)
        pre[n] = value

seq = [b]
if b not in pre:
    print 'NO'
else:
    print 'YES'
    x = b
    while x != a:
        x = pre[x]
        seq.append(x)
    print len(seq)
    for i in seq[::-1]:
        print i,
