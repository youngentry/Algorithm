import sys
input = sys.stdin.readline
import heapq

V,E = map(int,input().split())
K = int(input())

# 인접행렬 그리기
grid = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    grid[u].append((w,v))

# 초기 세팅
min_dis = 3000000
q = []
visited = [3000000]*(V+1)
visited[K] = 0
q.append((0,K)) # 시작점 넣기
while q:
    cost,des = heapq.heappop(q)
    if visited[des] < cost: # 기존 경로보다 크면 패스
        continue
    for dcost,ddes in grid[des]:
        new_cost = cost + dcost
        if new_cost < visited[ddes]: # 거리가 짧으면
            visited[ddes] = new_cost # 갱신
            heapq.heappush(q,(new_cost,ddes)) # 해당 경로에서 탐색 이어가기

for i in range(1,V+1):
    if visited[i] == 3000000:
        print("INF")
    else:
        print(visited[i])