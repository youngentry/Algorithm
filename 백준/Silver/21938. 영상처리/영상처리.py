import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
grid = []
for i in range(n):
    line = list(map(int,input().split()))
    row = []
    for j in range(0,len(line),3):
        aver = (line[j]+line[j+1]+line[j+2]) // 3
        row.append(aver)
    grid.append(row)
t = int(input())

# print(grid)
count = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] >= t:
            grid[i][j] = 255
        else:
            grid[i][j] = 0
# print(*grid,sep='\n')
directions = [[-1,0],[1,0],[0,1],[0,-1]]
visited = [[False]*m for _ in range(n)]
def bfs(start,end):
    queue = deque([[start,end]])
    while queue:
        x,y = queue.popleft()
        
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and grid[nx][ny]== 255 and visited[nx][ny] == False:
                grid[nx][ny] = 0
                visited[nx][ny] = True
                queue.append([nx,ny])
for i in range(n):
    for j in range(m):
        if grid[i][j] == 255:
            bfs(i,j)
            count += 1

print(count)