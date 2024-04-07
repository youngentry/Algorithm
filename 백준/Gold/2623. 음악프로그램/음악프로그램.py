import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())

in_degree = [0]*(N+1)
graph = {}
for i in range(1,N+1):
    graph[i] = []
# 단방향 간선 그래프, 진입 차수 배열 초기화
for i in range(M):
    cnt, *singers = map(int,input().split())
    for j in range(1, cnt):
        s,e = singers[j-1], singers[j]
        in_degree[e] += 1
        graph[s].append(e)

# 진입 차수가 0인 노드 q에 삽입
q = deque()
for i in range(1,N+1):
    if in_degree[i] == 0:
        q.append(i)

# 진입 차수를 감소시키며,
result = []
while q:
    cur = q.popleft()
    result.append(cur)
    for next in graph[cur]:
        in_degree[next] -= 1
        # 진입 차수가 0이 되는 노드를 q에 삽입
        if in_degree[next] == 0:
            q.append(next)

# 사이클 체크
if len(result) != N:
    print(0)
else:
    print(*result,sep="\n")
