import sys

input = sys.stdin.readline

n,s = map(int,input().split())

arr = [abs(s-i) for i in map(int,input().split())]

max_divisor = arr[0]

def ucle(a,divisor):
    global max_divisor
    while divisor>0:
        a,divisor = divisor,a%divisor
    max_divisor  = min(max_divisor,a)

for i in range(1,n):
    ucle(arr[i],max_divisor) 

print(max_divisor)