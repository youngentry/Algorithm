import sys
input = sys.stdin.readline
from collections import deque

N,M,K = map(int,input().split())
grid = [list(map(int,input().strip())) for _ in range(N)]
v = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]

if N==1 and M==1:
    print(1)
else:
    q = deque([(0,0,0,0)])
    grid[0][0] = [1]*(K+1)
    ans = 0
    while q:
        x,y,move,k = q.popleft()
        if x==N-1 and y==M-1:
            ans = move
            break
        for dx,dy in ((-1,0),(0,1),(1,0),(0,-1)):
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<M and grid[nx][ny] == 0 and v[nx][ny][k] == 0:
                v[nx][ny][k] = move+1
                q.append((nx,ny,move+1,k))
            if k<K and 0<=nx<N and 0<=ny<M and grid[nx][ny] == 1 and v[nx][ny][k+1] == 0:
                v[nx][ny][k+1] = move+1
                q.append((nx,ny,move+1,k+1))

    if ans:
        print(ans+1)
    else:
        print(-1)
