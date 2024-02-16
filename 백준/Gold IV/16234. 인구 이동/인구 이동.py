import sys
import math
from copy import deepcopy
from collections import deque

def transform(str_num):
    # 인구,상,우,하,좌
    return [int(str_num),False,False,False,False]

def init_visited(arr):
    for i in range(n):
        for j in range(n):
            arr[i][j] = 0

def bfs(start):
    global grid
    count_sum = 0
    count_sum += grid[start[0]][start[1]][0]
    visited_poses = [start]
    queue = deque([start])
    moved = False
    # print(start)
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            dx, dy = directions[i]
            nx,ny = x+dx, y+dy
            # 국경이 열려 있고, 해당 국가를 방문하지 않았다면
            # print(grid[x][y],x,y)
            if 0 <= nx < n and 0 <= ny < n and grid[x][y][i+1] and visited[nx][ny] == 0:
                moved = True
                visited[nx][ny] = 1
                count_sum += grid[nx][ny][0]
                queue.append([nx,ny])
                visited_poses.append([nx,ny])
    return [count_sum,visited_poses,moved]


# 입력 받기
n,low,high = map(int,input().split())
# n*n 격자
grid = [list(map(transform,input().split())) for _ in range(n)]
directions = [[-1,0],[0,1],[1,0],[0,-1]]
# print(*grid,sep='\n')

# 인구이동 진행할 수 없을 때까지 반복
move_count = 0
while True:
    visited = [[0] * (n) for _ in range(n)]
    init_visited(visited)

    # 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면,
    # 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
    for x in range(n):
        for y in range(n):
            for i in range(4):
                dx,dy = directions[i]
                nx,ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n and low <= abs(grid[x][y][0]-grid[nx][ny][0]) <= high:
                    grid[x][y][i+1] = True

    # 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
    # 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면,
    # 그 나라를 오늘 하루 동안은 연합이라고 한다.
    is_moved = False
    for x in range(n):
        for y in range(n):
            if visited[x][y] == 0:
                visited[x][y] = 1
                _sum,poses,moved = bfs([x,y])
                # 연합을 이루고 있는 각 칸의 인구수는
                # (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
                # print(_sum,poses,moved, math.floor(_sum / len(poses)))
                if moved:
                    is_moved = True
                    divided = math.floor(_sum / len(poses))
                    for i,j in poses:
                        # 연합을 해체하고, 모든 국경선을 닫는다.
                        grid[i][j] = [divided, False, False, False, False]

    # for row in grid:
    #     for col in row:
    #         print(col[0],end=' ')
    #     print()
    # print('---')

    if is_moved:
        move_count+=1
    else:
        break
# print(*grid,sep='\n')

# 각 나라의 인구수가 주어졌을 때,
# 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.
print(move_count)