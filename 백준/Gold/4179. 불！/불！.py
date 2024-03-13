import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int,input().split())
grid = []

start = None
fires = []
for i in range(R):
    line = list(input().strip())
    grid.append(line)
    for j in range(C):
        if line[j] == "J":
            start = (i,j,0,"J")
        elif line[j] == "F":
            fires.append((i,j,0,"F"))


q = deque([*fires,start])
while q:
    x,y,time,obj = q.popleft()
    # 나갈 수 있다면 종료
    if obj == "J" and (x==0 or x==R-1 or y==0 or y==C-1):
        print(time+1)
        break

    for dx,dy in ((-1,0),(0,1),(1,0),(0,-1)):
        nx,ny = x+dx,y+dy
        if 0<=nx<R and 0<=ny<C and obj == "F" and (grid[nx][ny] == "." or grid[nx][ny] == "J"):
            grid[nx][ny] = "F"
            q.append((nx,ny,time+1,"F"))
        elif 0<=nx<R and 0<=ny<C and obj == "J" and (grid[nx][ny] == "."):
            grid[nx][ny] = "J"
            q.append((nx,ny,time+1,"J"))
else:
    print('IMPOSSIBLE')