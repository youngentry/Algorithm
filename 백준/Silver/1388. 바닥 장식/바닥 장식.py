import sys
input = sys.stdin.readline

def dfs(i,j,base):
    v[i][j] = 1

    if base == "-":
        if j+1 < M and grid[i][j+1] == "-" and v[i][j+1] == 0:
            dfs(i,j+1,base)
    if base == "|":
        if i+1 < N and grid[i+1][j] == "|" and v[i+1][j] == 0:
            dfs(i+1,j,base)

N,M = map(int,input().split())
grid = [list(input().strip()) for _ in range(N)]
v = [[0]*M for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if v[i][j] == 0:
            if grid[i][j] == "-":
                dfs(i,j,"-")
            else:
                dfs(i,j,"|")
            ans += 1

print(ans)