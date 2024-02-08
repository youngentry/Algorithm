import sys
from collections import deque

input = sys.stdin.readline

m,n,b = map(int,input().split())

grid = []
for i in range(b):
    board = []
    for j in range(n):
        board.append(list(map(int,input().split())))
    # print(*board,sep='\n')
    grid.append(board)
# print(*grid,sep='\n')

starts = []

# 토마토 찾기
for i in range(b):   
    for j in range(n):    
        for k in range(m):
            if grid[i][j][k] == 1:
                starts.append([i,j,k])

# print(starts)
queue = deque([])
directions = [[-1,0,0],[1,0,0],[0,-1,0],[0,1,0],[0,0,-1],[0,0,1]]

def bfs():
    global max_count

    while queue:
        z,x,y,count = queue.popleft()


        for dz,dx,dy in directions:
            nz,nx,ny = z+dz,x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and 0<=nz<b and grid[nz][nx][ny] == 0:
                grid[nz][nx][ny] = 1
                max_count = max(max_count,count+1)
                queue.append([nz,nx,ny,count+1])

        # for board in grid:
        #     print(*board,sep='\n')

max_count = 0
for z,x,y in starts:
    if grid[z][x][y] == 1:
        queue.append([z,x,y,0])
bfs()

# print(max_count)

# 안 익은 토마토 찾기
is_ripen = True
for i in range(b):   
    for j in range(n):    
        for k in range(m):
            if grid[i][j][k] == 0:
                is_ripen = False

if is_ripen:
    print(max_count)
else:
    print(-1)