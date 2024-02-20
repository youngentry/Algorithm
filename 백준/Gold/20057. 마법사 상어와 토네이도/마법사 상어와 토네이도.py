import sys
import math
from collections import deque

# 좌 상 우 하
dots0 = [[-2,0,2],[-1,-1,10],[-1,0,7],[-1,1,1],[0,-2,5],[1,-1,10],[1,0,7],[1,1,1],[2,0,2]]
dots1 = [[info[1],-info[0],info[2]] for info in dots0]
dots2 = [[info[1],-info[0],info[2]] for info in dots1]
dots3 = [[info[1],-info[0],info[2]] for info in dots2]

dot_collection = [dots0,dots3,dots2,dots1]
directions = [[0,-1],[1,0],[0,1],[-1,0]] #좌하우상

def sweep(sx,sy,dir):
    global result
    b = grid[sx][sy] # 해당지점의 전체 모래 양
    a = b # 남은 모래
    grid[sx][sy] = 0

    for dx,dy,val in dot_collection[dir]:
        nx,ny = sx+dx,sy+dy
        thrown_dust = (b*val)//100
        a -= thrown_dust # 모래 제하기
        if 0<=nx<n and 0<=ny<n:
            grid[nx][ny] += thrown_dust # 날린 모래 더하기
        else:
            result += thrown_dust

    nx2,ny2 = sx+directions[dir][0], sy+directions[dir][1]
    if 0<=nx2<n and 0<=ny2<n:
        grid[nx2][ny2] += a # 날린 모래 더하기
    else:
        result += a



n = int(input().strip())
grid = [list(map(int,input().split())) for _ in range(n)]
result = 0


x, y = n // 2, n // 2
num = 1
draw_count = 1
ord = -1
dir = [[0, -1], [1, 0], [0, 1], [-1, 0]]

while num < n ** 2:
    for i in range(4):
        ord = (ord + 1) % 4
        dx, dy = dir[ord]

        for j in range(draw_count):
            if num >= n ** 2:
                break
            num += 1
            x, y = x + dx, y + dy
            sweep(x, y, ord)

        if i % 2 == 1:
            draw_count += 1

print(result)




