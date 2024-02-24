import sys
from copy import deepcopy
input = sys.stdin.readline 

# 입력 받기
N = 4
grid = []
for i in range(N):
    line = list(map(int,input().split()))
    tmp = [[-9,-9]]
    for j in range(0,N*2,2):
        tmp.append([line[j],line[j+1]])
    tmp.append([-9,-9])
    grid.append(tmp)
wall = [[-9,-9]]*(N+2)
grid.insert(0,wall)
grid.append(wall)

directions = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
max_sum = grid[1][1][0]
grid[1][1] = [-1,grid[1][1][1]]


# 이후 물고기가 이동한다.
# 물고기는 번호가 작은 물고기부터 순서대로 이동한다. 
# 물고기는 한 칸을 이동할 수 있고
# 이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸,
# 이동할 수 없는 칸은 상어가 있거나, 공간의 경계를 넘는 칸이다

# 이동할 수 있는 칸이 없으면 이동을 하지 않는다 *** 조건 충족하는지 확인 안함 ***
def fish_move(fish_grid):
    for k in range(1,17):
        for i in range(1,N+1):
            flag = False
            for j in range(1,N+1):
                fish_num, fish_ord = fish_grid[i][j]
                if fish_num == k: # 물고기 번호 작은순부터
                    # 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전
                    for ord in range(8):
                        di,dj = directions[(fish_ord-1+ord)%8][0],directions[(fish_ord-1+ord)%8][1]
                        ni,nj = i+di,j+dj
                        if fish_grid[ni][nj][0] > -1:
                            # 물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동
                            fish_grid[i][j][1] = (fish_ord-1+ord)%8 + 1
                            fish_grid[i][j], fish_grid[ni][nj] = fish_grid[ni][nj], fish_grid[i][j] 
                            flag = True
                            cell_flag = True
                            break
                if flag:
                    break
            if flag:
                break
    return fish_grid

# 물고기의 이동이 모두 끝나면 상어가 이동
# 상어는 방향에 있는 칸으로 이동할 수 있는데, 한 번에 여러 개의 칸을 이동할 수 있다
# 상어가 물고기가 있는 칸으로 이동했다면, 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가지게 된다
# 이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않는다
# 물고기가 없는 칸으로는 이동할 수 없다
# 상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다
#  ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 
# 상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다. 

def shark_move(shark_grid,cur_sum):
    is_shark_found = False
    shark_grids = []
    global max_sum

    # print(*shark_grid,sep='\n')
    # print('================', cur_sum)
    for i in range(1,N+1):
        if is_shark_found:
            break
        for j in range(1,N+1):
            if is_shark_found:
                break
            if shark_grid[i][j][0] == -1:
                shark_ord = shark_grid[i][j][1]
                for k in range(1,4):
                    di,dj = directions[shark_ord-1][0]*k, directions[shark_ord-1][1]*k
                    ni,nj = i+di,j+dj
                    if 1<=ni<N+1 and 1<=nj<N+1:
                        copied_shark_grid = deepcopy(shark_grid)
                        if copied_shark_grid[ni][nj][0] > 0:
                            tmp_sum = copied_shark_grid[ni][nj][0]
                            cur_sum += tmp_sum
                            max_sum = max(max_sum, cur_sum)
                            copied_shark_grid[ni][nj][0] = -1
                            copied_shark_grid[i][j] = [0,0]
                            is_shark_found = True
                            shark_grids.append([deepcopy(copied_shark_grid),cur_sum])
                            cur_sum -= tmp_sum
    return shark_grids


# fish_move(grid)

stack = [[grid,max_sum]]
while stack:
    cur_map,cur_sum = stack.pop()
    # print(cur_sum,"v")
    # print(len(stack),'len')
    # print(*cur_map,sep='\n')
    # print('-------')
    fish_grid = fish_move(cur_map)
    shks = shark_move(deepcopy(fish_grid),cur_sum)
    if shks:
        for shk in shks:
            stack.append(shk)

print(max_sum)
# 상어가 이동한 후에는 다시 물고기가 이동하며, 이후 이 과정이 계속해서 반복