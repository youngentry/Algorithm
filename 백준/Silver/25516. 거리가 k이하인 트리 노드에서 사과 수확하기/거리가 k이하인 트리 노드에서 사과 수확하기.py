import sys
input = sys.stdin.readline
from collections import deque

# ===================================================

N,K = map(int,input().split())

graph = [[] for _ in range(N)]

for i in range(N-1):
    s,e = map(int,input().split())
    graph[s].append(e)

apples = list(map(int,input().split()))
ans = 0
if apples[0]:
    ans += 1
q = deque()
q.append((0,K))
v = [0] * N
v[0] = 1
while q:
    s,dist = q.popleft()
    if dist == 0:
        continue
    for ns in graph[s]:
        if v[ns] == 0:
            v[ns] = 1
            if apples[ns]:
                ans +=1
            q.append((ns,dist-1))
print(ans)
# ===================================================
