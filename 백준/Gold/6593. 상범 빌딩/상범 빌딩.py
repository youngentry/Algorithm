import sys
from collections import deque
import heapq
import time
input = sys.stdin.readline
# st = time.time()
# ======================================

def bfs(sk,sx,sy):
    q = deque([(sk,sx,sy,0)])
    grid[sk][sx][sy] = "#"
    exit_cnt = 0
    while q:
        k,x,y,move = q.popleft()
        for dk,dx,dy in ((-1,0,0),(1,0,0),(0,-1,0),(0,0,1),(0,1,0),(0,0,-1)):
            nk,nx,ny = k+dk,x+dx,y+dy
            if 0<=nk<L and 0<=nx<R and 0<=ny<C and grid[nk][nx][ny] != "#":
                if grid[nk][nx][ny] == "E":
                    exit_cnt = move+1
                grid[nk][nx][ny] = "#"
                q.append((nk,nx,ny,move+1))
    return exit_cnt

while True:
    L,R,C = map(int,input().split())

    if L==0 and R==0 and C==0:
        break

    grid = []
    start = None
    end = None
    for k in range(L):
        floor = []
        for i in range(R):
            row = list(input().strip())
            floor.append(row)
            for j in range(C):
                if row[j] == "S":
                    start = (k,i,j)
                elif row[j] == "E":
                    end = (k,i,j)

        grid.append(floor)
        null = input()

    min_dist = bfs(*start)
    if min_dist == 0:
        print("Trapped!")
    else:
        print(f'Escaped in {min_dist} minute(s).')
# ======================================
# print(time.time() - st)