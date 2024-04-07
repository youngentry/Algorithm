import sys
input = sys.stdin.readline
from collections import deque

# start_time = time.time()
# ======================================

N,M = map(int,input().split())
in_degree = [0]*(1+N)
graph = {}
for i in range(1,N+1):
    graph[i] = []


for i in range(M):
    a,b = map(int,input().split())

    in_degree[b] += 1
    graph[a].append(b)

q = deque()
for i in range(1,N+1):
    if in_degree[i] == 0:
        q.append(i)
result = []
while q:
    cur = q.popleft()
    result.append(cur)

    for next in graph[cur]:
        in_degree[next] -= 1
        if in_degree[next] == 0:
            q.append(next)

print(" ".join(map(str,result)))


# ======================================
# print(time.time() - start_time)
