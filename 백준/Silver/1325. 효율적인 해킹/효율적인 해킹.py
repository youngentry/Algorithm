import sys
input = sys.stdin.readline
from collections import deque


def bfs(sx):
    v[sx] = 1
    cnt = 0
    q = deque([sx])
    while q:
        cx = q.popleft()
        for nx in adj[cx]:
            if v[nx]:
                continue

            v[nx] = 1
            cnt += 1
            q.append(nx)
    return cnt

# 무방향그래프
N,M = map(int,input().split())

adj = [[] for _ in range(N+1)]

for i in range(M):
    s,e = map(int,input().split())
    adj[e].append(s)

mx = 0
result = []
for i in range(1,N+1):
    v = [0]*(N+1)
    tmp_cnt = bfs(i)
    result.append((i,tmp_cnt))

result.sort(key=lambda x:(x[1],x[0]))

mx = result[-1][1]
for num,cnt in result:
    if cnt == mx:
        print(num,end=" ")