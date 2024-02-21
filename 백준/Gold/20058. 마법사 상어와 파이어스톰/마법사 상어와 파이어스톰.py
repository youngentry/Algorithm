import sys
import math
from collections import deque

n,q = map(int,input().split())
base_size = 2**n
grid = [list(map(int,input().split())) for _ in range(base_size)]
magics = list(map(int,input().split()))

# 1) L**Li 만큼의 격자로 나누고 90도 회전시킴
# 2) 얼음 녹일 좌표 저장, 해당 좌표 일제히 녹이기

def rotate(arr,x,y):
    global grid

    size = len(arr)
    rotated_grid = [[0]*size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            rotated_grid[j][size-1-i] = arr[i][j]

    for i in range(x,size+x):
        for j in range(y,size+y):
            grid[i][j] = rotated_grid[i-x][j-y]


def divide(arr,cur_size,target_try,x,y):
    if cur_size == 2**target_try:
        # 회전시키기
        rotate(arr,x,y)
        return

    size = len(arr)
    s1 = []
    s2 = []
    s3 = []
    s4 = []
    half_size = size//2
    for i in range(size):
        for j in range(2):
            if i < half_size and j==0:
                s1.append(arr[i][:half_size])
            elif i < half_size and j==1:
                s2.append(arr[i][half_size:])
            elif i >= half_size and j==0:
                s3.append(arr[i][:half_size])
            elif i >= half_size and j==1:
                s4.append(arr[i][half_size:])

    divide(s1, half_size, target_try,x,y)
    divide(s2, half_size, target_try,x,y+half_size)
    divide(s3, half_size, target_try,x+half_size,y)
    divide(s4, half_size, target_try,x+half_size,y+half_size)

directions = [[-1,0],[0,1],[1,0],[0,-1]]

for magic in magics:
    divide(grid,base_size,magic,0,0)

    melt_pos = []
    # 녹일 좌표 저장
    for i in range(base_size):
        for j in range(base_size):
            adj = 0
            for di,dj in directions:
                ni,nj = i+di, j+dj

                # no_adj = 0
                # 범위 안이라면
                if 0<=ni<base_size and 0<=nj<base_size:
                    if grid[ni][nj]:
                        adj += 1
                    # else:
                    #     no_adj += 1
                # 범위 밖이라면
                # else:
                #     no_adj += 1

            if adj < 3:
                melt_pos.append((i,j))

    for i,j in melt_pos:
        if grid[i][j] > 0:
            grid[i][j] -= 1

count = 0
for i in range(base_size):
    for j in range(base_size):
        count += grid[i][j]

def bfs(start):
    queue = deque([])
    queue.append(start)
    grid[start[0]][start[1]] = 0
    move_count = 0
    while queue:
        x,y = queue.popleft()
        for dx,dy in directions:
            nx,ny = x+dx, y+dy
            if 0<=nx<base_size and 0<=ny<base_size and grid[nx][ny]:
                move_count += 1
                grid[nx][ny] = 0
                queue.append((nx,ny))
    return move_count
# print(*grid,sep='\n')

chunk_count = 0
for i in range(base_size):
    for j in range(base_size):
        if grid[i][j]:
            move_result = bfs((i,j)) + 1
            chunk_count = max(chunk_count, move_result)
print(count)
print(chunk_count)