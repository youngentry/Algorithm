import sys
input = sys.stdin.readline
from collections import deque

q = deque()
def find_target_BFS(sx,sy,tgrid):
    q.append((sx,sy,D-1))
    v = [[0]*M for _ in range(N)]
    v[sx][sy] = 1

    while q:
        x,y,d = q.popleft()
        if not d: # 사거리 넘어서면 종료
            continue
        for dx,dy, in ((0,-1),(-1,0),(0,1)):
            nx,ny, = x+dx,y+dy
            if 0<=nx<N and 0<=ny<M and v[nx][ny]==0:
                if tgrid[nx][ny]: # 대상을 탐색한 경우 대상 반환하고 종료
                    q.clear()
                    return (nx,ny)

                v[nx][ny] = 1
                q.append((nx,ny,d-1))


def defence(rangers):
    global ans

    tgrid = [grid[i][:] for i in range(N)]
    kill_cnt = 0
    remain_cnt = enemy_cnt

    ranger_poses = []
    for i in range(M):
        if rangers[i]:
            ranger_poses.append((N-1,i))
    while remain_cnt:
        kill_poses = set()
        for k in range(3):
            rx,ry = ranger_poses[k] # 레인저 좌표
            if tgrid[rx][ry]: # 시작 지점이면 바로 반환
                kill_poses.add((rx, ry))
                continue
            else: # 아니면 공격할 대상 탐색
                target_pos = find_target_BFS(rx,ry,tgrid)
                if target_pos:
                    kill_poses.add(target_pos)

        for x,y in kill_poses:
            tgrid[x][y] = 0
            kill_cnt += 1
            remain_cnt -= 1

        # 적군 이동
        for i in range(N,0,-1): # 아래에서 위로 올라가며 확인
            for j in range(M):
                if i == N: # 성에 도달한 경우
                    if tgrid[i-1][j]:
                        tgrid[i-1][j] = 0
                        remain_cnt -= 1
                else: # 아닌 경우는 아래로 이동
                    tgrid[i][j],tgrid[i-1][j] = tgrid[i-1][j],tgrid[i][j]

    ans = max(ans, kill_cnt)


def dfs(n,start):
    if n==3:
        defence(rangers)
        return

    for i in range(start,M):
        rangers[i] = 1
        dfs(n+1,i+1)
        rangers[i] = 0


N,M,D = map(int,input().split())
grid = []
enemy_cnt = 0
for i in range(N):
    line = list(map(int,input().split()))
    for j in range(M):
        if line[j] == 1:
            enemy_cnt += 1
    grid.append(line)

ans = 0
rangers = [0]*M
dfs(0,0)

print(ans)
