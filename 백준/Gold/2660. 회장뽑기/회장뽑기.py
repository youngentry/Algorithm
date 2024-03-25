import sys
from collections import deque

def bfs(sx):
    q = deque([(sx,0)])
    v = [0] * (N+1)
    v[sx] = 1

    mx_dist = 0
    while q:
        x,dist = q.popleft()
        mx_dist = max(mx_dist, dist)

        for nx in graph[x]:
            if v[nx] == 1:
                continue

            v[nx] = 1
            q.append((nx,dist+1))

    return mx_dist


N = int(input())
graph = [ [] for _ in range(N+1)]

while True:
    s,e = map(int, input().split())

    if s==-1 and e==-1:
        break

    graph[s].append(e)
    graph[e].append(s)

result_list = []
for i in range(1,N+1):
    score = bfs(i)
    result_list.append((score,i))

result_list.sort()

mn_score = result_list[0][0]
candidates = []
for i in range(N):
    if result_list[i][0] == mn_score:
        candidates.append(result_list[i][1])

print(mn_score, len(candidates))
print(" ".join(map(str,candidates)))
