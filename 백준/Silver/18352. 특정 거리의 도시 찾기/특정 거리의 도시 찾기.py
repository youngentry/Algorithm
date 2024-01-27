import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int,input().split())

grid = {}

# 도시 개수 n
for i in range(n):
    grid[i+1] = []

# 도로 개수 m
for i in range(m):
    start,end = map(int,input().split())
    grid[start].append([end,0])

# 최단거리 k
queue = deque([[x,0]])
result = []
visited = [0]*(n+1)
visited[x] = 1
while queue:
    start, val = queue.popleft()

    if val == k:
        result.append(start)

    for at,at_val in grid[start]:

        if visited[at] == 0:
            visited[at] = 1
            queue.append([at, val+1]) 

if len(result):
    print(*sorted(result), sep="\n")
else:
    print(-1)