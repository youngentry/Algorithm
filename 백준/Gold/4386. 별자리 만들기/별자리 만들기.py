import sys
input = sys.stdin.readline
import heapq

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(float,input().split())))

# 인접행렬 만들기
adjs = [ [] for _ in range(N) ]
for i in range(N):
    for j in range(N):
        if i != j:
            x1,y1 = arr[i]
            x2,y2 = arr[j]
            adjs[i].append([round(((x2-x1)**2 + (y2-y1)**2)**0.5,2),j])

# Prim 알고리즘
pq = []
sm = 0
v = [0]*N
heapq.heappush(pq, [0,0])
while pq:
    dist,s = heapq.heappop(pq)

    if v[s] == 1:
        continue # 처리된 노드는 넘기기
    v[s] = 1

    sm += dist
    for ndist, ne in adjs[s]:
        if v[ne] == 1:
            continue # 이미 방문한 노드라면 넘기기
        heapq.heappush(pq, (ndist,ne)) # 다음 간선을 heappush로 추가

print(sm)