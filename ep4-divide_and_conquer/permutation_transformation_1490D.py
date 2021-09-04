def permutation(vetor, left_idx, right_idx, h):
    if right_idx - left_idx <= 0: return
    max_value = max(vetor[left_idx:right_idx])
    tree[max_value] = h
    permutation(vetor, left_idx, vetor.index(max_value), h+1)
    permutation(vetor, vetor.index(max_value)+1, right_idx, h+1)

t = int(input())

for i in range(t):
    tree = {}
    n = int(input())
    a = list(map(int, input().split()))
    permutation(a, 0, n, 0)
    out = str(tree[a[0]])
    for e in range(1, len(a)):
        out += ' ' + str(tree[a[e]])
    print(out)