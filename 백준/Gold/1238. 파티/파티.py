import sys
input = sys.stdin.readline
from heapq import heappush, heappop

INF = int(2e9)

def dijkstra(graph, sx, N):
    v = [INF] * (N + 1)
    v[sx] = 0
    pq = [(0, sx)]

    while pq:
        w, x = heappop(pq)

        if w > v[x]:
            continue

        for dw, nx in graph[x]:
            nw = w + dw
            if nw < v[nx]:
                v[nx] = nw
                heappush(pq, (nw, nx))
    return v

# 입력 받기
input = sys.stdin.readline
N, M, X = map(int, input().split())

# 그래프와 역방향 그래프 초기화
graph = [[] for _ in range(N+1)]
reverse_graph = [[] for _ in range(N+1)]

# 그래프 입력 받기 및 역방향 그래프 생성
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))
    reverse_graph[e].append((w, s))  # 역방향 그래프에 추가

# X에서 시작하는 다익스트라 알고리즘 실행
dist_from_X = dijkstra(graph, X, N)

# 역방향 그래프에서 X로의 다익스트라 알고리즘 실행
dist_to_X = dijkstra(reverse_graph, X, N)

# 최대 시간 계산
mx_time = 0
for i in range(1, N+1):
    if i != X:
        mx_time = max(mx_time, dist_from_X[i] + dist_to_X[i])

print(mx_time)