import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

# 바이러스 조합을 생성하고, 퍼뜨리고, 되돌리기 반복
def bfs(poses):
    global min_time
    # print(*poses)
    queue = deque(*poses)
    max_time = 0 # 이동 시간
    floor_count = len(floors)
    while queue:
        # print(floor_count)
        x,y,time = queue.popleft()
        # print(max_time,"max_time",time,"time")
        max_time = max(max_time,time)
        if floor_count == 0:
            continue
        else:
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if grid[nx][ny] != 1:
                    if grid[nx][ny] == 0: # 0 개수 확인
                        floor_count -= 1
                    grid[nx][ny] = 1
                    queue.append([nx,ny,time+1])
    # print(min_time,max_time)
    # print(*grid,sep='\n')
    for i in range(1,n+1):
        for j in range(1,n+1):
            if grid[i][j] == 0:
                return
    min_time = min(min_time,max_time) # 최소 시간 설정

# 좌표 복원
def init_virus():
    global floors
    global viruses
    
    for floor in floors:
        grid[floor[0]][floor[1]] = 0
    for virus in viruses:
        grid[virus[0]][virus[1]] = 2

n,m = map(int,input().split())
wall = [[1]*(n+2)]
grid = wall+[[1]+list(map(int,input().split()))+[1] for _ in range(n)]+wall
directions = [[-1,0],[0,1],[1,0],[0,-1]]    
min_time = 987654321
# print(*grid,sep='\n')

# 복원할 좌표
viruses = []
floors = []
for i in range(1,n+1):
    for j in range(1,n+1):
        if grid[i][j] == 2:
            viruses.append([i,j,0])
        elif grid[i][j] == 0:
            floors.append([i,j])
# print(viruses,"viruses")
# print(floors,"floors")

# 놓을 수 있는 바이러스가 더 많은 엣지 케이스가 있음?
if len(viruses) < m:
    virus_combs = list(combinations(viruses,len(viruses)))
else:
    virus_combs = list(combinations(viruses,m))

# print(virus_combs,"virus_combs")

for virus_comb in virus_combs:
    for sx,sy,move in virus_comb:
        grid[sx][sy] = 1

    bfs([virus_comb])
    init_virus()

if min_time == 987654321:
    print(-1)
else:
    print(min_time)