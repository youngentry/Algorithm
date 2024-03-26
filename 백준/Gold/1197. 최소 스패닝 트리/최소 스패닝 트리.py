import sys
from heapq import heappop, heappush
from collections import deque

def prim(sx):
    pq = [(0,sx)]
    w_acc = 0
    cnt = N
    while pq:
        w,x = heappop(pq)

        if v[x] == 1:
            continue

        v[x] = 1
        w_acc += w
        cnt -= 1

        for nw,nx in graph[x]:
            if v[nx]:
                continue

            heappush(pq, (nw,nx))

        if cnt == 0:
            break
    print(w_acc)


N,M = map(int,input().split())
graph = [ [] for _ in range(N+1)]
v = [0] * (N+1)
for i in range(M):
    s,e,w = map(int,input().split())
    graph[s].append((w,e))
    graph[e].append((w,s))

prim(1)