import sys
from collections import deque
input = sys.stdin.readline 


################################# 입력받기 ################################
def transform(str_int):
    return [int(str_int)]

# N:격자크기, M:상어 수, K:이동횟수
N,M,K = map(int,input().split())
sharks = [0]*(M+1) # 상어 위치정보 (방향,x,y)
grid = []
for i in range(N):
    line = list(map(transform,input().split()))
    grid.append(line)
    for j in range(N):
        sharks[line[j][0]] = [line[j][0],i,j]
sharks[0] = [-1,-1,-1]
smells = [[[0,0] for _ in range(N)] for _ in range(N)] # 냄새 정보

for i in range(N):
    for j in range(N):
        if grid[i][j][0] == 0:
            grid[i][j] = deque()
        else:
            grid[i][j] = deque([grid[i][j][0]])

sdirs = list(map(int,input().split()))
for i in range(1,M+1):
    x,y = sharks[i][1],sharks[i][2]
    sharks[i][0] = sdirs[i-1]
    
priorities = [[] for _ in range(M)] # 각 상어의 방향 정보
for i in range(M):
    for j in range(4):
        priorities[i].append(list(map(int,input().split())))
################################# 입력받기 ################################
sharks,smells,grid,priorities = sharks,smells,grid,priorities
directions = [[-1,0],[1,0],[0,-1],[0,1]] # 상하좌우

# 자신의 위치에 냄새 뿌리기
def smell():
    for i in range(1,M+1):
        if sharks[i]:
            _,x,y = sharks[i]
            smells[x][y] = [i,K] # 자신의 냄새를 그 칸에 뿌린다

def del_smell():
    # 냄새 한 번 지우기
    for i in range(N):
        for j in range(N):
            if smells[i][j][1]-1 >= 0 :
                smells[i][j][1] -= 1
                if smells[i][j][1] == 0: # 냄새는 상어가 k번 이동하고 나면 사라진다
                    smells[i][j] = [0,0] 

# 1의 번호를 가진 어른 상어는 가장 강력해서 나머지 모두를 쫓아낼 수 있다.

# 그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고, 

# 모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면,
# 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.


# print(*priorities,sep='\n')

# 상어 이동

# 상어 이동 
def move():


    for i in range(1,len(sharks)):
        is_moved = False
        if sharks[i]:
            dir,x,y = sharks[i]
            
            # 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다
            no_smells = []
            yes_smells = []
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if 0<=nx<N and 0<=ny<N and smells[nx][ny][0] == 0:
                    no_smells.append((nx,ny))
                    yes_smells.append(None)
                elif 0<=nx<N and 0<=ny<N and smells[nx][ny][0] == i:
                    no_smells.append(None)
                    yes_smells.append((nx,ny))

                else:
                    no_smells.append(None)
                    yes_smells.append(None)

            # 냄새가 없는 칸 이동
            for pri_num in priorities[i-1][dir-1]: # 특정한 우선순위를 따른다
                if no_smells[pri_num-1]:
                    nsx,nsy = no_smells[pri_num-1]
                    sharks[i][0], sharks[i][1], sharks[i][2] = pri_num, nsx, nsy
                    is_moved = True
                    pop_shark = grid[x][y].popleft()
                    if not grid[nsx][nsy]:
                        grid[nsx][nsy].append(pop_shark)
                    elif grid[nsx][nsy] and grid[nsx][nsy][-1] > i:
                        grid[nsx][nsy].append(pop_shark)
                    else:
                        grid[nsx][nsy].appendleft(pop_shark)

                    break

            # 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다
            # 이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 
            if not is_moved:
                for pri_num in priorities[i-1][dir-1]: # 특정한 우선순위를 따른다
                    if yes_smells[pri_num-1]:
                        nsx,nsy = yes_smells[pri_num-1]
                        sharks[i][0], sharks[i][1], sharks[i][2] = pri_num, nsx, nsy
                        pop_shark = grid[x][y].popleft()
                        if not grid[nsx][nsy]:
                            grid[nsx][nsy].append(pop_shark)
                        elif grid[nsx][nsy] and grid[nsx][nsy][-1] > i:
                            grid[nsx][nsy].append(pop_shark)
                        else:
                            grid[nsx][nsy].appendleft(pop_shark)
                        break
    # print(sharks,"sharkssharks")
        
    # print(*grid,sep='\n')

    kill_sharks()
    del_smell()
    smell()
                    # 방금 이동한 방향이 보고 있는 방향이 된다.

shark_count = M
def kill_sharks():
    global shark_count

    for i in range(N):
        for j in range(N):
            while len(grid[i][j]) > 1:
                killed_shark = grid[i][j].popleft()
                shark_count -= 1
                sharks[killed_shark] = None
                # print(killed_shark,"killed_shark")
                # print(sharks,"sharks")


smell() # 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다
time = 0
while shark_count > 1 and time <= 1000:
    time +=1
    move()
    # print(sharks)
    # print(*smells,sep='\n')

if time == 1001:
    print(-1)
else:
    print(time)