import sys
input = sys.stdin.readline
from collections import deque

dirs = ((-1,0),(0,1),(1,0),(0,-1))
def bfs(sx,sy,num):
    q = deque([(sx,sy)])
    grid[sx][sy] = num

    while q:
        x,y = q.popleft()
        for dx,dy in dirs:
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and grid[nx][ny] == 1:
                grid[nx][ny] = num
                q.append((nx,ny))

borders = []
def bfs2(sx,sy):
    q = deque([(sx,sy)])
    grid[sx][sy] = 1

    while q:
        x,y = q.popleft()
        for dx,dy in dirs:
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and grid[nx][ny] == 0:
                grid[nx][ny] = 1
                q.append((nx,ny))
            elif 0<=nx<N and 0<=ny<N and grid[nx][ny] > 1:
                borders.append((nx,ny,grid[nx][ny],0))



N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

flag = False
# 아무 0 찾기
ch_pos = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 0:
            ch_pos.append((i,j))

# 섬 번호 부여
cnt = 10
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            bfs(i,j,cnt)
            cnt += 1

# print(*grid,sep='\n')

for x,y in ch_pos:
    if grid[x][y] == 0:
        bfs2(x,y)

# print(*grid,sep='\n')

for i in range(N):
    for j in range(N):
        grid[i][j] = [grid[i][j],0]
bq = deque([*borders])
ans = []
while bq:
    x, y, num, move = bq.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and grid[nx][ny][0] == 1:
            grid[nx][ny] = [num,move+1]
            bq.append((nx, ny,num, move+1))
        elif 0 <= nx < N and 0 <= ny < N and grid[nx][ny][0] > 1 and grid[nx][ny][0] != num:
            ans.append(move+grid[nx][ny][1])
            # borders.append((nx, ny, grid[nx][ny],move+1))

# print(ans)
# print(*grid,sep='\n')

print(min(ans))
