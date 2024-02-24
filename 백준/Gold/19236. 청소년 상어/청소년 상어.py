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

#  ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 
directions = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
max_sum = grid[1][1][0]
grid[1][1] = [-1,grid[1][1][1]]


# 물고기 이동
# 이동할 수 있는 칸이 없으면 이동X => *** 조건 충족하는지 확인X. 못 움직이는 케이스가 안 떠오름 ***
def fish_move(fish_grid):
    # 물고기는 번호가 작은 물고기부터 순서대로 이동한다. 
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
                        # 이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸
                        if fish_grid[ni][nj][0] > -1:
                            # 물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동
                            fish_grid[i][j][1] = (fish_ord-1+ord)%8 + 1
                            fish_grid[i][j], fish_grid[ni][nj] = fish_grid[ni][nj], fish_grid[i][j] 
                            flag = True
                            break
                if flag:
                    break
            if flag:
                break
    return fish_grid

# 물고기가 없는 칸으로는 이동할 수 없다
# 상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다. 
# 상어 이동
def shark_move(in_grid,cur_sum):
    global max_sum

    new_shark_grids = []
    for i in range(1,N+1):
        for j in range(1,N+1):
            if in_grid[i][j][0] == -1:
                shark_ord = in_grid[i][j][1]
                # 방향에 있는 칸으로 한 번에 여러 개의 칸을 이동할 수 있다
                for k in range(1,4):
                    di,dj = directions[shark_ord-1][0]*k, directions[shark_ord-1][1]*k
                    ni,nj = i+di,j+dj
                    if 1<=ni<N+1 and 1<=nj<N+1:
                        # 상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다
                        if in_grid[ni][nj][0] > 0:
                            # 물고기가 있는 칸으로 이동했다면, 
                            copied_shark_grid = deepcopy(in_grid) # 새로운 경로
                            tmp_sum = copied_shark_grid[ni][nj][0]
                            cur_sum += tmp_sum # # 그 칸에 있는 물고기를 먹고,
                            max_sum = max(max_sum, cur_sum) # 최대값 갱신
                            copied_shark_grid[ni][nj][0] = -1 # 해당 칸으로 이동, 그 물고기의 방향을 가지게 된다
                            copied_shark_grid[i][j] = [0,0] # 먹힌 물고기는 제거
                            new_shark_grids.append([copied_shark_grid,cur_sum]) # 새로운 경로 탐색
                            cur_sum -= tmp_sum # 백트래킹
            if new_shark_grids:
                return new_shark_grids

# 상어가 이동한 후에는 다시 물고기가 이동하며, 이후 이 과정이 계속해서 반복
stack = [[grid,max_sum]]
while stack:
    cur_map,cur_sum = stack.pop()
    fish_grid = fish_move(cur_map) # 물고기 이동 결과
    shark_moves = shark_move(fish_grid,cur_sum) # 물고기 이동 후, 상어 이동 결과

    # 상어 이동 결과가 있다면 stack에 추가
    if shark_moves:
        for shk in shark_moves:
            stack.append(shk)

print(max_sum)