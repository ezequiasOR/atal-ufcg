import math

n = int(input())
s = list(map(int,input().split()))

num_one = s.count(1)
num_two = s.count(2)
num_three = s.count(3)
num_four = s.count(4)

taxis = num_four + num_three

if num_one <= num_three:
    taxis = taxis + math.ceil(num_two / 2)
else :
    taxis = taxis + math.ceil((num_two * 2 + num_one - num_three) / 4)

print(taxis)
