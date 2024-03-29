import sys
from heapq import heappush, heappop

INF = int(2e9)
def dijkstra(sx):
    global mx_time

    v = [INF]*(N+1)
    v[sx] = 0
    pq = [(0,sx)]

    while pq:
        w,x = heappop(pq)

        if w > v[x]:
            continue

        for dw,nx in graph[x]:
            nw =w+dw
            if nw < v[nx]:
                v[nx] = nw
                heappush(pq,(nw,nx))
    return v


N,M,X = map(int,input().split())

students = [ i for i in range(1,N+1)]
graph = [[] for _ in range(N+1)]
for i in range(M):
    s,e,w = map(int,input().split())
    graph[s].append((w,e))

mx_time = 0
base_v = dijkstra(X)
for num in students:
    if num != X:
        temp_v = dijkstra(num)
        if temp_v[X] != INF:
            mx_time = max(mx_time, temp_v[X]+base_v[num])

print(mx_time)