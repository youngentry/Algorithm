import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

N,M,K = map(int,input().split()) 
balls = [list(map(int,input().split())) for _ in range(M)]
grid = [[deque([]) for _ in range(N)] for _ in range(N)]

dir = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

for i in range(M):
    # m:질량, d:방향, s:속력
    r,c,m,s,d = balls[i]
    grid[r-1][c-1].append((r-1,c-1,m,s,d))
    # balls[i] = r-1,c-1,m,d,s

# print(*grid,sep='\n')

time = 0
while time < K :
    time += 1

    # 파이어볼 위치 찾기
    new_balls = []
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                for t_ball in grid[i][j]:
                    new_balls.append(t_ball)

    # print(new_balls)
    # 이동하기
    for i in range(len(new_balls)):
        r,c,m,s,d = new_balls[i]
        dr,dc = dir[d][0]*s, dir[d][1]*s
        grid[r][c].popleft()
        grid[(r+dr)%N][(c+dc)%N].append(((r+dr)%N,(c+dc)%N,m,s,d))
    # print(*grid,sep='\n')

    # 같은 칸 합치기
    for i in range(N):
        for j in range(N):
            if len(grid[i][j])>=2:
                tmp_m = 0
                tmp_s = 0
                odd = 0
                even = 0
                for t_ball in grid[i][j]:
                    tmp_m += t_ball[2]
                    tmp_s += t_ball[3]
                    
                    if t_ball[4] % 2 == 0:
                        even += 1
                    else:
                        odd += 1
                divided_m = tmp_m//5
                divided_s = tmp_s//len(grid[i][j])
                
                # print(*grid,sep='\n')
                # print(divided_m,"??????????????????????????????????")

                if divided_m == 0:
                    grid[i][j].clear()
                    continue
                else:
                    tmp_dirs = []
                    if odd==0 or even==0:
                        for q in range(0,8,2):
                            tmp_dirs.append(q)
                    else:
                        for q in range(1,8,2):
                            tmp_dirs.append(q)
                    tmp_list = []
                    for tmp_dir in tmp_dirs:
                        tmp_list.append((i,j,divided_m,divided_s,tmp_dir))
                    # print(tmp_list,"??????")
                    grid[i][j] = deque(tmp_list)
    # print(*grid,sep='\n')

# print(*grid,sep='\n')

m_sum = 0
for i in range(N):
    for j in range(N):
        if grid[i][j]:
            for ball in grid[i][j]:
                m_sum += ball[2] 
print(m_sum)