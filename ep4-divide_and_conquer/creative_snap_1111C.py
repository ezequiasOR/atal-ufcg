n, k, a, b = map(int, input().split())
base = [0] * (k)
p = input().split()
for i in range(len(p)):
    base[i] = int(p[i])-1


def power(base, left, right):
    base_length = len(base)

    if base_length == 0:
        return a
    elif left == right:
        return base_length * b

    base_left = []
    base_right = []
    base_half_length = (left + right) // 2

    for e in base:
        if left <= e <= base_half_length:
            base_left += [e]
        if base_half_length + 1 <= e <= right:
            base_right += [e]
    return min(b * base_length * (right - left + 1),
               power(base_left, left, base_half_length) +
               power(base_right, base_half_length + 1, right))


print(power(base, 0, 2 ** n - 1))
