import sys
from collections import deque
from itertools import combinations, permutations
from math import sqrt, ceil
from copy import deepcopy

input = sys.stdin.readline

n,m = map(int,input().split())

grid = []
chicken_coord = []
# 지도 생성
for i in range(n):
    line = list(map(int,input().split()))
    # 치킨집 추가
    for j in range(n):
        if line[j] == 2:
            chicken_coord.append([i,j])
            line[j] = 0
    grid.append(line)

# print(grid)
# print(chicken_coord)

# 치킨집 조합 생성
combs = list(combinations(chicken_coord,m))
# print(combs)

# def bfs(temp_grid):
#     cur_min = 987654321
#     # print(*temp_grid,sep='\n')
#     while queue:
#         x,y,move = queue.popleft()
#         for dx,dy in directions:
#             nx,ny = x+dx, y+dy
#             if 0<=nx<n and 0<=ny<n and temp_grid[nx][ny] != 9:
#                 if temp_grid[nx][ny] == 2:
#                     cur_min = min(cur_min,move+1)
#                     queue.clear()
#                     return cur_min
#                 temp_grid[nx][ny] = 9
#                 queue.append([nx,ny,move+1])

directions = [[-1,0],[0,1],[1,0],[0,-1]]
min_distance = 987654321
dists = []
# 폐업 시뮬레이션 지도 생성
for chickens in combs:
    dist = []
    copied_grid = deepcopy(grid)
    # print(chickens)
    # 치킨집 지도 설정
    for x,y in chickens:
        copied_grid[x][y] = 2
    # print(*copied_grid,sep='\n')

    # queue = deque([])
    # 1에 대해 각각의 최단 거리의 합 저장
    for i in range(n):
        for j in range(n):
            if copied_grid[i][j] == 1:
                min_dist = 987654321
                for k in range(n):
                    for l in range(n):
                        if copied_grid[k][l] == 2:
                            
                            min_dist = min(min_dist, abs(i-k)+abs(j-l))
                dist.append(min_dist)
                # temp = deepcopy(copied_grid)
                # temp[i][j] = 9
                # queue.append([i,j,0])
                # dist.append(bfs(temp))
                # min_distance =min(min_distance,bfs(temp)) 
    dists.append(sum(dist))

print(min(dists))






