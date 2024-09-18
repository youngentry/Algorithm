import math
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
sr,sc,gr,gc = map(int,input().split())

board = [[0]*N for _ in range(N)]
board[sr][sc] = 1

q = deque([(sr,sc,0)])
while q:
    r,c,move = q.popleft()

    if r == gr and c == gc:
        print(move)
        break

    for dx,dy in ((-2,-1),(-2,+1),(0,-2),(0,2),(2,-1),(2,1)):
        nx,ny = r+dx,c+dy
        if 0<=nx<N and 0<=ny<N and board[nx][ny] == 0:
            board[nx][ny] = 1
            q.append((nx,ny,move+1))
else:
    print(-1)