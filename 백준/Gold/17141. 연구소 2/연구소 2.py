import sys
from  collections import  deque
input = sys.stdin.readline

def bfs(pathes):
    global space
    global M

    q = deque([])
    tmp_v = [row[:] for row in v]

    for px,py in pathes:
        tmp_v[px][py] = 1
        q.append((px,py,0))
    tmp_space = space-M

    mx_move = 0
    while q:
        x,y,move = q.popleft()

        for dx,dy in dirs:
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<N and tmp_v[nx][ny] != 1:
                if tmp_v[nx][ny] == 0:
                    tmp_v[nx][ny] = 1
                    tmp_space -= 1
                    if tmp_space == 0:
                        q.clear()
                        mx_move = max(mx_move, move+1)
                        break
                q.append((nx,ny,move+1))

    for i in range(N):
        for j in range(N):
            if tmp_v[i][j] == 0:
                return 987654321
    return mx_move


def dfs(n,start):
    global M
    global virus_cnt
    global mn_time

    if n==M:
        # bfs 작업수행
        mn_time = min(mn_time,bfs(path))
        return

    for i in range(start,virus_cnt):
        path.append(viurses[i])
        dfs(n+1,i+1)
        path.pop()


# N: 크기, M: 놓을 바이러스 수
N,M = map(int,input().split())
grid = []
viurses = []
space = 0
dirs = ((-1,0),(0,1),(1,0),(0,-1))
v = [[0]*N for _ in range(N)]
for i in range(N):
    line = list(map(int,input().split()))
    for j in range(N):
        if line[j] == 2:
            viurses.append((i,j))
            space += 1
        if line[j] == 0:
            space += 1
        if line[j] == 1:
            v[i][j] = 1
    grid.append(line)
path = []
virus_cnt = len(viurses)
mn_time = 987654321
dfs(0,0)

if space == 0:
    print(0)
elif mn_time == 987654321:
    print(-1)
else:
    print(mn_time)

