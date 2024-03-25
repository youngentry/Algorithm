import sys
from collections import deque
input = sys.stdin.readline

# ======================================
dirs = ((-1,0),(0,1),(1,0),(0,-1))
def bfs(sx,sy):
    q = deque([(sx,sy)])
    tmp_v = [v[i][:] for i in range(5)]
    tmp_v[sx][sy] = 0
    cnt = 1
    while q:
        x,y = q.popleft()
        for dx,dy in dirs:
            nx,ny = x+dx,y+dy
            if 0<=nx<5 and 0<=ny<5 and tmp_v[nx][ny] == 1:
                tmp_v[nx][ny] = 0
                cnt += 1
                q.append((nx,ny))
    if cnt == 7:
        return True
    return False


def is_adjacent():
    for i in range(5):
        for j in range(5):
            if v[i][j] == 1:
                return bfs(i,j)


def dfs(n,start,ycnt,scnt):
    global ans
    if ycnt >= 4:
        return

    if n==7:
        if is_adjacent():
            ans += 1
        return

    for i in range(start,N):
        v[i//5][i%5] = 1
        if arr[i] == 'Y':
            dfs(n+1,i+1,ycnt+1,scnt)
        else:
            dfs(n+1,i+1,ycnt,scnt+1)
        v[i//5][i%5] = 0


N = 25
v = [[0]*5 for _ in range(5)]
arr = []
for i in range(5):
    arr += list(input().strip())

ans = 0
dfs(0,0,0,0)

print(ans)
# ======================================
