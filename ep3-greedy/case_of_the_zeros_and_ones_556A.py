n = int(input())
s = list(input())

count_one = 0
count_zero = 0

for e in s:
    if e == '1':
        if count_one <= 0:
            count_zero += 1
        else:
            count_one -= 1
    else:
        if count_zero <= 0:
            count_one += 1
        else:
            count_zero -= 1

print(count_zero + count_one)
