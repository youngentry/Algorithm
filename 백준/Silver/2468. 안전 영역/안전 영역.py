import sys
from collections import deque
import copy

input = sys.stdin.readline

n = int(input())

grid = []
for i in range(n):
    grid.append(list(map(int,input().split())))

results = []
def bfs(start,grid):
    safe_count = 0
    queue = deque([start])
    while queue:
        # print(queue)
        x,y = queue.popleft()
        for dx,dy in directions:
            nx, ny = x+dx, y+dy
            if nx>=0 and ny>=0 and nx<n and ny<n and grid[nx][ny]==0:
                grid[nx][ny] = 1
                safe_count+=1
                queue.append([nx,ny])
    return safe_count

for k in range(1,100):
    # 지대 높이 정보 저장
    tmp_grid = copy.deepcopy(grid)

    # 완전탐색으로 안전지대 0, 잠긴지대 1로 구분
    for i in range(n):
        for j in range(n):
            if tmp_grid[i][j] <= k:
                tmp_grid[i][j] = 1
            else:
                tmp_grid[i][j] = 0

    # bfs로 안전지대 탐색하여 지역 정보 저장
    safe_areas = []
    directions = [[-1,0],[0,1],[1,0],[0,-1]]
    for i in range(n):
        for j in range(n):
            if tmp_grid[i][j] == 0:
                safe_areas.append(bfs([i,j],tmp_grid))

    results.append(len(safe_areas))

if max(results)==0:
    print(1)
else:
    print(max(results))