import sys

input = sys.stdin.readline

n, m = map(int,input().split())

_set = set()
lst = []

for _ in range(n):
    line = input().strip() 
    _set.add(line)

for _ in range(m):
    line = input().strip() 
    if line in _set:
        lst.append(line)

print(len(lst))

if len(lst):
    print(*sorted(lst),sep="\n")

