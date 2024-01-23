import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

# 그래프 그리기
graph = {}
for i in range(1,n+1):
    graph[i]=[]
for _ in range(m):
    start,end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [0] * (n+1)

count = 0

for i in range(1,n+1):
    if visited[i] == 0:
        visited[i]=1
        count+=1

        queue = deque([i])
        while queue:
            start = queue.popleft()
            for num in graph[start]:
                if visited[num]==0:
                    visited[num]=1
                    queue.append(num)

print(count)

# 그래프 만들기
# 1부터 끝까지 방문
# BFS를 돌 때마다 count +1

