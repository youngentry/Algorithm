import sys
from collections import deque
input = sys.stdin.readline

# bfs로 빙하 확인
q = deque()
def bfs(sx,sy):
    q.append((sx,sy))
    v[sx][sy] == 0
    while q:
        x,y = q.popleft()
        for dx,dy in dirs:
            nx,ny = dx+x,dy+y
            if 0<=nx<N and 0<=ny<M and v[nx][ny] != 0:
                v[nx][ny] = 0
                q.append((nx,ny))

                
N,M= map(int,input().split())
grid = []
zeros = []                              # 바다 영역 찾기
for i in range(N):
    line = list(map(int,input().split()))
    grid.append(line)
    for j in range(M):
        if line[j] == 0:
            zeros.append((i,j))


# 3. 계속 반복하기
time = 0
dirs = ((-1,0),(0,1),(1,0),(0,-1))
is_all_melted = False
while True:
    time += 1

    for i in range(len(zeros)-1,-1,-1): # 1. 바다 주변 녹이기
        x,y = zeros[i]
        sea_count = 0                   # 해당 바다 지점의 사면이 바다인지 확인
        for dx,dy in dirs:
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<M and grid[nx][ny] != 0:
                grid[nx][ny] -= 1
                if grid[nx][ny] == 0:   # 바닷물로 변했으면 zeros에 추가
                    zeros.append((nx,ny))
                    sea_count += 1
            else:
                sea_count += 1    
        
        if sea_count == 4:              # 사면이 바다면 pop하여 제거
            zeros.pop(i)

    bfs_count = 0                       # 2. BFS로 확인하기
    v = [row[:] for row in grid]
    for i in range(N):
        for j in range(M):
            if v[i][j] != 0:
                bfs(i,j)
                bfs_count += 1
    if bfs_count >= 2:                  # 2 이상이라면 분리된 것
        break
    elif bfs_count == 0:                # 0 이라면 모두 동시에 녹은 것
        print(0)
        is_all_melted = True
        break
        
if not is_all_melted:
    print(time)