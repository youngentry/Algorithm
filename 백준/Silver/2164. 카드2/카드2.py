import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
what = deque([i+1 for i in range(n-1,-1,-1)])

while len(what)>1:
    drop = what.pop()
    go_bot = what.pop()
    what.appendleft(go_bot)

print(what[0])