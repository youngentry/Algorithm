import sys
from collections import deque
from copy import deepcopy

n = int(input())
grid = []
for _ in range(n):
    grid.append(list(input().strip()))


directions = [[-1,0],[0,1],[1,0],[0,-1]]

queue = deque([])
def bfs(i,j, map):
    target = map[i][j]
    map[i][j] = 0
    while queue:
        x,y = queue.popleft()
        for dx,dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and map[nx][ny] == target:
                map[nx][ny] = 0
                queue.append([nx,ny])

grid_normal = deepcopy(grid)
normal_count = 0
for i in range(n):
    for j in range(n):
        if grid_normal[i][j]:
            queue.append([i,j])
            bfs(i,j,grid_normal)
            normal_count += 1

grid_weak = deepcopy(grid)
for i in range(n):
    for j in range(n):
        if grid_weak[i][j] == "G":
            grid_weak[i][j]="R"
weak_count = 0
for i in range(n):
    for j in range(n):
        if grid_weak[i][j]:
            queue.append([i,j])
            bfs(i,j,grid_weak)
            weak_count += 1

print(normal_count,weak_count)
