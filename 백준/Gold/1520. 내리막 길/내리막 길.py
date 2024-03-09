import sys
input = sys.stdin.readline


def dfs(x,y):
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for dx,dy in dirs:
        nx,ny = x+dx,y+dy
        if 0<=nx<N and 0<=ny<M and grid[x][y] > grid[nx][ny]:
            dp[x][y] += dfs(nx,ny)
    
    return dp[x][y]

N,M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
dirs = [[-1,0],[0,1],[1,0],[0,-1]]

dp = [[-1]*M for _ in range(N)]
dp[N-1][M-1] = 1
dfs(0,0)

print(dfs(0,0))