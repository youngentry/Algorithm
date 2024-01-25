import sys

input = sys.stdin.readline

n,m = map(int,input().split())
numbers = [0] + list(map(int,input().split()))

# 누적합 구하기
_sum = 0
for i in range(1,n+1):
    _sum += numbers[i]
    numbers[i] = _sum

# 구간 합 구하기
for _ in range(m):
    start,end = map(int,input().split())
    print(numbers[end] - numbers[start-1])
    