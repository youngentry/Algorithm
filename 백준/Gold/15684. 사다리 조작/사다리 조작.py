import sys
input = sys.stdin.readline

def check():
    for i in range(1,M+1):
        cx = 0
        cy = i
        for j in range(N):
            if grid[cx][cy]:
                cy += 1
            elif grid[cx][cy-1]:
                cy -= 1
            cx +=1
        if cx == N and cy != i:
            return False

    return True


def dfs(n,start):
    global pos_cnt
    global mx_ladder
    global is_good

    if n==mx_ladder:
        if check():
            is_good = True
        return

    for i in range(start,pos_cnt):
        x,y = poses[i]
        if grid[x][y-1] or grid[x][y+1]:
            continue
        grid[x][y] = 1
        dfs(n+1,i+1)
        grid[x][y] = 0


M,K,N = map(int,input().split())
grid = [[0]*(M+2) for _ in range(N)]

for i in range(K):
    a, b = map(int,input().split())
    grid[a-1][b] = 1

poses = []
for i in range(N):
    for j in range(1,M):
        if grid[i][j] == 0 and grid[i][j-1] == 0 and grid[i][j+1] == 0:
            poses.append((i,j))
pos_cnt = len(poses)
ans = 4
for i in range(4):
    mx_ladder = i
    path = []
    is_good = False
    dfs(0,0)
    if is_good:
        ans = min(ans,i)
        break
if ans == 4:
    print(-1)
else:
    print(ans)
