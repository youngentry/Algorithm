import sys
from math import floor
input = sys.stdin.readline

# 청정기 탐색
def find_cleaner():
    global grid
    tmp_cleaner = []
    for j in range(R):
        if grid[j][0] == -1:
            tmp_cleaner.append([j,0])
            tmp_cleaner.append([j+1,0])
            break
    return tmp_cleaner

# 5이상인 먼지 좌표 탐색
def find_dusts():
    global grid
    tmp_dusts = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] >= 5:
                tmp_dusts.append([i,j])
    return tmp_dusts

# 먼지 하나의 확산 함수
def _spread(pos_x_y):
    global grid
    x,y = pos_x_y
    count = 0 # 몇 방향 확산
    plus = floor(grid[x][y]/5) # 확산할 수치
    spread_pos_x_y = [] # 확산될 좌표
    for dx,dy in directions:
        nx,ny = x+dx, y+dy
        if 0<=nx<R and 0<=ny<C and grid[nx][ny] != -1:
            spread_pos_x_y.append([nx,ny])
            count += 1
    minus = plus*count # 마이너스할 수치
    return [pos_x_y, spread_pos_x_y, plus, minus]

# 미세먼지 확산될 정보 수집
def get_dust_spread_infos(mage_dust_info):
    tmp_results = []
    for pos_x_y in mage_dust_info:
        # x,y 좌표에 minus spread_pos에 plus 하면 됨
        tmp_results.append(_spread(pos_x_y))
    return tmp_results

# 미세먼지 확산
def spread_all_dusts(mage_info):
    global grid
    for result in mage_info:
        base,spread_pos_x_y,plus,minus = result
        grid[base[0]][base[1]] -= minus
        for x,y in spread_pos_x_y:
            grid[x][y] += plus

# 공기청정기 작동 (역순으로 한 칸씩 당기기)
def circulate(cleaner_pos_x_y):
    global grid
    up,down = cleaner_pos_x_y
    up_x = up[0]
    down_x = down[0]
    grid[up_x-1][0] = 0
    grid[down_x+1][0] = 0
    # down
    for i in range(up_x-1,0,-1):
        grid[i][0] = grid[i-1][0]
    # left
    for j in range(0,C-1):
        grid[0][j] = grid[0][j+1]
    # up
    for i in range(0,up_x):
        grid[i][C-1] = grid[i+1][C-1]
    # right
    for j in range(C-1,1,-1):
        grid[up_x][j] = grid[up_x][j-1]
    grid[up_x][1] = 0

    # up
    for i in range(down_x+1,R-1):
        grid[i][0] = grid[i+1][0]
    # left
    for j in range(0,C-1):
        grid[R-1][j] = grid[R-1][j+1]
    # down
    for i in range(R-1,down_x,-1):
        grid[i][C-1] = grid[i-1][C-1]
    # right
    for j in range(C-1,1,-1):
        grid[down_x][j] = grid[down_x][j-1]
    grid[down_x][1] = 0

R,C,T = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(R)]
directions = [[-1,0],[0,1],[1,0],[0,-1]]
cleaner = find_cleaner()

time = 0
while time < T:
    time += 1
    dusts = find_dusts()
    spread_infos = get_dust_spread_infos(dusts)
    spread_all_dusts(spread_infos)
    circulate(cleaner)

count = 2
for i in range(R):    
    for j in range(C):    
        count += grid[i][j]

print(count)