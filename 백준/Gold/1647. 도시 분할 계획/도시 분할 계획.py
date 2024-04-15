import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N, M = map(int,input().split())

# 양방향 간선
# 유지비
# 마을 두 개로 분할
# 최소 경로

adjs = [[] for _ in range(N+1)]
v = [0]*(N+1)

for i in range(M):
    s,e,w = map(int,input().split())
    adjs[s].append((w,e))
    adjs[e].append((w,s))

pq = [(0,1)]
rst = []

sm = 0
mx = 0
while pq:
    cw, cur = heappop(pq)

    if v[cur]:
        continue
    v[cur] = 1
    mx = max(mx,cw)
    sm += cw
    for nw, next in adjs[cur]:
        heappush(pq, (nw,next))

print(sm - mx)