# A. IQ test - (https://codeforces.com/problemset/problem/25/A)

n = int(input())
num = list(map(int, input().split()))

even = {'qty': 0, 'idx': 0, 'flag': False}
odd = {'qty': 0, 'idx': 0, 'flag': False}

for i in range(len(num)):
    if(num[i] % 2 == 0):
        even['qty'] += 1
        even['idx'] = i
    else:
        odd['qty'] += 1
        odd['idx'] = i

if even['qty'] == 1:
    even['idx'] += 1
    even['flag'] = True
if odd['qty'] == 1:
    odd['idx'] += 1
    odd['flag'] = True

if even['flag']:
    print(even['idx'])
elif odd['flag']:
    print(odd['idx'])
else:
    print(0)
