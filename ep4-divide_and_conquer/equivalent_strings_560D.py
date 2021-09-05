def equivalency(s):
    s_lenght = len(s)

    if s_lenght % 2 != 0:
        return s

    s_half_lenght = s_lenght // 2
    s1 = equivalency(s[0:s_half_lenght])
    s2 = equivalency(s[s_half_lenght:s_lenght])

    if s1 < s2:
        return s1 + s2
    else:
        return s2 + s1


l1 = input()
l2 = input()

if equivalency(l1) == equivalency(l2):
    print('YES')
else:
    print('NO')
