import sys

input = sys.stdin.readline

n,k = map(int,input().split())

numbers = [i+1 for i in range(n)]
lst = []

idx = k-1
while numbers:
    lst.append(numbers.pop(idx))
    if len(numbers) != 0:
        idx = (idx + k-1) % len(numbers) 

print("<" +str(lst)[1:-1] + ">")