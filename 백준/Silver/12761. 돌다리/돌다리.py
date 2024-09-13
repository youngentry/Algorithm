import sys
from _collections import deque
from copy import deepcopy

A,B,N,M = map(int,input().split())

# a 또는 b 만큼 이동 가능
# n이 m으로 향해야 함

# 현위치 +1,-1,+A,-A,+B,-B,A*n,B*n

arr = [0] * 100_001
v = [0] * 100_001
q = deque([(N,0)])
v[N] = 1

while q:
    cur,move = q.popleft()
    if cur == M:
        print(move)
        break

    if 0<= cur+1 <= 100_000 and v[cur+1] == 0:
        v[cur+1] = 1
        q.append((cur+1,move+1))
    if 0<= cur-1 <= 100_000 and v[cur-1] == 0:
        v[cur-1] = 1
        q.append((cur-1,move+1))
    if 0<= cur-A <= 100_000 and v[cur-A] == 0:
        v[cur-A] = 1
        q.append((cur-A,move+1))
    if 0<= cur+A <= 100_000 and v[cur+A] == 0:
        v[cur+A] = 1
        q.append((cur+A,move+1))
    if 0<= cur+B <= 100_000 and v[cur+B] == 0:
        v[cur+B] = 1
        q.append((cur+B,move+1))
    if 0<= cur-B <= 100_000 and v[cur-B] == 0:
        v[cur-B] = 1
        q.append((cur-B,move+1))
    if 0<= cur*A <= 100_000 and v[cur*A] == 0:
        v[cur*A] = 1
        q.append((cur*A,move+1))
    if 0<= cur*B <= 100_000 and v[cur*B] == 0:
        v[cur*B] = 1
        q.append((cur*B,move+1))


