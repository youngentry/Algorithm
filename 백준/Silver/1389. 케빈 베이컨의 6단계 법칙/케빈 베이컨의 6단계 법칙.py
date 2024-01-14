import sys
from collections import deque

def input():
  return tuple(map(int,sys.stdin.readline().split()))

n,k = input()

# 인원만큼 그래프 초기화
graph= {}
for i in range(1,n+1):
  graph[i] = []

# 그래프 생성
for _ in range(k):
  start, end = input()
  graph[start].append(end) 
  graph[end].append(start) 

# print(graph)
visited = [[0]*(n+1) for _ in range(n+1)]
# print(visited)

def bfs(start):
  queue = deque([start])
  # visited[start][start] = 
  
  while len(queue):
    user_num = queue.popleft()
    # print(graph[user_num])
    for num in graph[user_num]:
      # print(num)
      if not visited[start][num]:
        visited[start][num] = visited[start][user_num] + 1 
        queue.append(num)

  visited[start][start] = 0
    # print(visited)
      
for i in range(1,n+1):
  bfs(i)

# print(visited)
sums = []
for row in visited:
  _sum = sum(row)
  if _sum != 0:
    sums.append(sum(row))

print(sums.index(min(sums))+1)