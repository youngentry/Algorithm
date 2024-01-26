import sys

input = sys.stdin.readline

n = int(input())

a_nums =sorted( list(map(int,input().split())),reverse=True)
b_nums =sorted( list(map(int,input().split())))

result = 0

for i in range(n):
    result += a_nums[i]*b_nums[i]

print(result)