import sys
from _collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())

grid = [[0]*(M+1) for _ in range(N+1)]
grid[0][0] = 1

blocked_load = set()
K = int(input())
for i in range(K):
    a,b,c,d = map(int,input().split())
    blocked_load.add((a,b,c,d))
    blocked_load.add((c,d,a,b))

q = deque([(0,0,0)])
while q:
    x,y,acc = q.popleft()

    for dx,dy in ((1,0),(0,1)):
        nx,ny = x+dx,y+dy
        if (
                0<=nx<=N and
                0<=ny<=M and
                ((x,y,nx,ny) not in blocked_load or
                (nx,ny,x,y) not in (blocked_load)) and
                grid[nx][ny] == 0
            ):
            # 왼쪽벽
            if nx == 0:
                grid[nx][ny] = 1
                q.append((nx,ny,1))
            # 윗벽
            elif ny == 0:
                grid[nx][ny] = 1
                q.append((nx,ny,1))
            # 그외
            else:
                acc_x = grid[nx-1][ny]
                acc_y = grid[nx][ny-1]
                if (
                    ((nx, ny, nx - 1, ny) in blocked_load or
                     (nx - 1, ny, nx, ny) in blocked_load)
                    ):
                    acc_x = 0
                if (
                    ((nx,ny-1,nx,ny) in blocked_load or
                    (nx,ny,nx,ny-1) in blocked_load)
                    ):
                    acc_y = 0
                if acc_x + acc_y:
                    grid[nx][ny] = acc_x + acc_y
                    q.append((nx,ny,grid[nx][ny]))

print(grid[N][M])