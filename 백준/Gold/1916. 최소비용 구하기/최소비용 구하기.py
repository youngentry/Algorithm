import sys
import heapq

input = sys.stdin.readline

# 입력
n = int(input()) # 도시 수
m = int(input()) # 버스 수
# 버스 가중치 그래프
maxsize = sys.maxsize
distances = []
graph = []
for i in range(n+1):
    distances.append(maxsize)
    graph.append([])
# 버스 간선 그래프 세팅
for i in range(m):
    start, end, dis = map(int,input().split())
    graph[start].append((end,dis))
start,end = map(int,input().split())

# 시작점 설정
distances[start] = 0
queue = []
heapq.heappush(queue, [distances[start], start])
# 다익스트라 수행
while queue:
    cur_dis,cur_des = heapq.heappop(queue) # 가중치가 가장 낮은 경로 꺼내기
    
    # 기존 경로보다 크면 패스
    if distances[cur_des] < cur_dis:
        continue
    
    # 새 인접 경로 확인
    for new_des, new_dis in graph[cur_des]:
        forward_dis = cur_dis + new_dis
        if forward_dis < distances[new_des]: # 이동 결과가 지금까지 알던 거리보다 짧으면
            distances[new_des] = forward_dis # 짧은 거리로 갱신
            heapq.heappush(queue,[forward_dis, new_des]) # 해당 경로에서 탐색 이어가기

print(distances[end])