import sys
from collections import deque

n,m = map(int,input().split())
shop_count = int(input())
numbers = []
for _ in range(shop_count):
    numbers.append(list(map(int,input().split()))+[9])
start = list(map(int,input().split()))
numbers.append(start+[5])


grid = [[1]+[0]*(n-1)+[1] for _ in range(m-1)]
grid.append([1]*(n+1))
grid.insert(0,[1]*(n+1))

width = n+1
height = m+1
# print(width,height,n,m)
# 1북, 2남, 3서, 4동
for i,j,target in numbers:
    if i == 1:
        grid[0][j] = target
    if i == 2:
        grid[m][j] = target
    if i == 3:
        grid[j][0] = target
    if i == 4:
        grid[j][n] = target

directions = [[0,1],[0,-1],[1,0],[-1,0]]


where = None
for i in range(height):
    for j in range(width):
        if grid[i][j] == 5:
            where = [i,j,0]

# print(where)
queue = deque([where])
count = 0
while queue:
    # print('-----------------------')
    # print(*grid,sep='\n')
    x,y,move = queue.popleft()
    for dx,dy in directions:
        nx,ny = x+dx,y+dy
        if 0<=nx<height and 0<=ny<width and (grid[nx][ny] == 1 or grid[nx][ny] == 9):
            if grid[nx][ny] == 9:
                count += move+1
            grid[nx][ny] = 0
            queue.append([nx,ny,move+1])
print(count)