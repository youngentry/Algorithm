import sys
input = sys.stdin.readline
from collections import deque

# ===================================================

def bfs(sx,sy,base):
    global power_w
    global power_b

    cnt = 1
    grid[sx][sy] = "."

    q = deque()
    q.append((sx,sy))
    while q:
        x,y = q.popleft()
        for dx,dy in ((-1,0),(0,1),(1,0),(0,-1)):
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<M and grid[nx][ny] != ".":
                if grid[nx][ny] == base:
                    grid[nx][ny] = "."
                    cnt += 1
                    q.append((nx,ny))
    return cnt**2


M,N = map(int,input().split())
grid = [list(input().strip()) for _ in range(N)]

power_w = 0
power_b = 0

for i in range(N):
    for j in range(M):
        if grid[i][j] != ".":
            base = grid[i][j]
            power = bfs(i,j,base)
            if base == "W":
                power_w += power
            else:
                power_b += power

print(power_w,power_b)

# ===================================================
