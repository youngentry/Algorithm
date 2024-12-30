import sys
import math
input = sys.stdin.readline

N, X = map(int,input().split())
visitors = list(map(int,input().split()))
cur_sum = sum(visitors[:X])
max_sum = cur_sum
period_count = 1
for i in range(1,N-X+1):
    cur_sum = cur_sum - visitors[i-1] + visitors[i+X-1]
    if cur_sum > max_sum:
        max_sum = cur_sum
        period_count = 1
    elif cur_sum == max_sum:
        period_count += 1

if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(period_count)