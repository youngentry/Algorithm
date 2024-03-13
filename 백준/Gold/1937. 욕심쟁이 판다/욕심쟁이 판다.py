import sys
sys.setrecursionlimit(25000)
input = sys.stdin.readline

def dfs(x,y):
    # 이미 방문했다면 반환
    if v[x][y] != -1:
        return v[x][y]

    mx = 0
    for dx,dy in ((-1,0),(0,1),(1,0),(0,-1)):
        nx,ny = x+dx,y+dy
        if 0<=nx<N and 0<=ny<N and grid[x][y] < grid[nx][ny]:
            # 사방 탐색을 통해 가장 큰 값을 반환하는 stack 탐색
            mx = max(mx,dfs(nx,ny))

    # 해당 좌표에 가장 큰 값+1(최소한 한 칸이 배정됨)을 저장
    v[x][y] = mx + 1
    return v[x][y]


N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]
v = [[-1]*N for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        if v[i][j] == -1:
            ans = max(ans, dfs(i, j))

print(ans)
