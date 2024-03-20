import sys
from  collections import  deque
input = sys.stdin.readline

q = deque()
dirs = ((-1,0),(0,1),(1,0),(0,-1))
def bfs(pathes,g,r):
    global mx
    global size

    tmp_v = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                tmp_v[i][j] = [grid[i][j],1]
            else:
                tmp_v[i][j] = [grid[i][j],0]

    # g,r 배양토에 넣기
    for i in range(size):
        if v[i] == 3:
            q.append((grounds[i][0],grounds[i][1],3,1))
            tmp_v[grounds[i][0]][grounds[i][1]] = [3,1]
        elif v[i] == 4:
            q.append((grounds[i][0],grounds[i][1],4,1))
            tmp_v[grounds[i][0]][grounds[i][1]] = [4,1]

    while q:
        x,y,color,time = q.popleft()
        time += 1
        for dx,dy in dirs:
            nx,ny = x+dx,y+dy
            # 0:호수, color:자기색상, 5:꽃
            if 0<=nx<N and 0<=ny<M and (tmp_v[nx][ny][1] == 0 or tmp_v[nx][ny][1] == time):
                # 꽃이라면 확산 중지
                if tmp_v[x][y][0] == 5:
                    continue
                # 땅이면 퍼뜨리기
                if tmp_v[nx][ny][0] == 1 or tmp_v[nx][ny][0] == 2:
                    tmp_v[nx][ny] = [color,time]
                    q.append((nx,ny,color,time))
                # 다른 꽃이면 꽃 피우기
                elif color == 3 and tmp_v[nx][ny][0] == 4 and tmp_v[nx][ny][1] == time:
                    tmp_v[nx][ny] = [5,time]
                elif color == 4 and tmp_v[nx][ny][0] == 3 and tmp_v[nx][ny][1] == time:
                    tmp_v[nx][ny] = [5,time]

    # 꽃 개수 카운트
    cnt = 0
    for i in range(N):
        for j in range(M):
            if tmp_v[i][j][0] == 5:
                cnt += 1
    mx = max(mx,cnt)


def dfs(n,rc,gc,v):
    global G
    global R
    global size

    if gc > G:
        return
    if rc > R:
        return

    # 최대 시도 후 종료
    if rc+gc == G+R:
        bfs(path,G,R)
        return

    if n == size:
        return

    v[n] = 0
    dfs(n+1,rc,gc,v)
    v[n] = 3
    dfs(n+1,rc+1,gc,v)
    v[n] = 4
    dfs(n+1,rc,gc+1,v)
    v[n] = 0

N,M,G,R = map(int,input().split())
grid = []
grounds = []
for i in range(N):
    line = list(map(int,input().split()))
    grid.append(line)
    for j in range(M):
        if line[j] == 2:
            grounds.append((i,j))

path = []
mx = 0
size = len(grounds)
v = [0]*(size)
dfs(0,0,0,v)
print(mx)

