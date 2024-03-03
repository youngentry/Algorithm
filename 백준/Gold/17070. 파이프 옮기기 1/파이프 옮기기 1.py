# 좌표와, 머리 방향을 전달,
# 다음으로 이동가능한 경우에는 이동시킴
# 도달한 경우 ans+1
def dfs(i,j,dr):
    global ans

    if (i,j) == (N-1,N-1):
        ans += 1

    # >>>가로인 경우
    if (dr==0 or dr==1) and i<N and j+1<N and grid[i][j+1] == 0:
        dfs(i,j+1,0)
    # >>>대각인 경우
    if i+1<N and j+1<N and grid[i][j+1] == 0 and grid[i+1][j+1] == 0 and grid[i+1][j] == 0:
        dfs(i+1,j+1,1)
    # >>>세로인 경우
    if (dr==2 or dr==1) and i+1<N and j<N and grid[i+1][j] == 0:
        dfs(i+1,j,2)


N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]
ans = 0
dfs(0,1,0)

print(ans)
