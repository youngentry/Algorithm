import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

graph = {}
for i in range(1,n+1):
    graph[i] = []
for i in range(1,n):
    start, end = map(int,input().split())
    graph[start].append(end) 
    graph[end].append(start) 

memo = [0]*(n+1)
visited = [0]*(n+1)

queue = deque()
queue.append(1)
# memo[1] = -1
# visited[1] = 1

while len(queue):
    cur_node = queue.popleft()

    if visited[cur_node] == 0:
    # 현재 노드가 접근할 수 있는 노드 확인 
        next_nodes = graph[cur_node] # [1,3]
        for next_node in next_nodes: # 1,3
            if memo[next_node] == 0:
                memo[next_node] = cur_node
                queue.append(next_node)
            # # 부모 노드 체크
            # if memo[cur_node] != -1 and visited[next_node] == 1 and memo[next_node] != 0:
            #     memo[cur_node] = next_node # memo[6] = 1
            
            # visited[cur_node] = 1
            # queue.extend(graph[cur_node])

for num in (memo[2:]):
    print(num)



# 1. 트리를 그린다.
# 2. 이미 방문된 노드가 부모다.
# 3. BFS의 queue에 추가한다.