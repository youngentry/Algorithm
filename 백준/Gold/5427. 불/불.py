import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    C, R = map(int,input().split())
    grid = []

    start = None
    fires = []
    for i in range(R):
        line = list(input().strip())
        grid.append(line)
        for j in range(C):
            if line[j] == "@":
                start = (i,j,0,"@")
            elif line[j] == "*":
                fires.append((i,j,0,"*"))


    q = deque([*fires,start])
    while q:
        x,y,time,obj = q.popleft()
        # 나갈 수 있다면 종료
        if obj == "@" and (x==0 or x==R-1 or y==0 or y==C-1):
            print(time+1)
            break

        for dx,dy in ((-1,0),(0,1),(1,0),(0,-1)):
            nx,ny = x+dx,y+dy
            if 0<=nx<R and 0<=ny<C and obj == "*" and (grid[nx][ny] == "." or grid[nx][ny] == "@"):
                grid[nx][ny] = "*"
                q.append((nx,ny,time+1,"*"))
            elif 0<=nx<R and 0<=ny<C and obj == "@" and (grid[nx][ny] == "."):
                grid[nx][ny] = "@"
                q.append((nx,ny,time+1,"@"))
    else:
        print('IMPOSSIBLE')