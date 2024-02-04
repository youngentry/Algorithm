import sys

input = sys.stdin.readline

n= int(input())
target = int(input())

grid = [[0]*n for _ in range(n)]

count = n**2
direction = "D"
x,y = 0,0
for i in range(n*n,0,-1):
    grid[x][y] = i
    
    if direction=="D":
        if x+1==n or grid[x+1][y] != 0:
            direction="R"
            y+=1
        else:
            x+=1
    elif direction=="R":
        if y+1==n or grid[x][y+1] != 0:
            direction="U"
            x-=1
        else:
            y+=1
    elif direction=="U":
        if x==0 or grid[x-1][y] != 0:
            direction="L"
            y-=1
        else:
            x-=1
    elif direction=="L":
        if y==0 or grid[x][y-1] != 0:
            direction="D"
            x+=1
        else:
            y-=1

for i in grid:
    print(" ".join(map(str,i)))
 
for i in range(n):
    for j in range(n):
        if grid[i][j] == target:
            print(i+1,j+1)