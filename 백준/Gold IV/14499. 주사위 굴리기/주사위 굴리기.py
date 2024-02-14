import sys
from collections import deque
from math import floor
input = sys.stdin.readline

n,m,x,y,k = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
orders = list(map(int,input().split()))

#     위
# 왼 천장 오
#    아래
#    바닥
dice = [
    [-1, 0, -1, -1],
    [0,  0,  0,  0],
    [-1, 0, -1, -1],
    [-1, 0, -1, -1]
 ]

def get_top():
    print(f'{dice[1][1]}')
    return dice[1][1]

def get_bot():
    print(dice[1][3])
    return dice[1][3]


# 회전
# 1:동 row[1]+1, 2:서 col[1]-1
# 3:남 col[1]+1, 4:북 col[1]-1
directions = [None, [0, 1], [0, -1], [-1, 0], [1, 0]]
def rotate(pos, dir):
    cx,cy = pos
    dx,dy = directions[dir]
    nx,ny = cx+dx, cy+dy
    # 지도 바깥으로 이동하려면 무시
    if not 0<=nx<n or not 0<=ny<m:
        # print(dir,nx,ny,"????????????????")
        return False

    # 주사위 회전
    if dir == 4:
        tmp = dice[1][3]
        for i in range(3,0,-1):
            dice[i][1] = dice[i-dx][1]
        dice[0][1] = tmp
        dice[1][3] = dice[3][1]
    elif dir == 3:
        tmp = dice[0][1]
        for i in range(0,3):
            dice[i][1] = dice[i-dx][1]
        dice[3][1] = tmp
        dice[1][3] = dice[3][1]
    elif dir == 2:
        tmp = dice[1][0]
        for i in range(0,3):
            dice[1][i] = dice[1][i-dy]
        dice[1][3] = tmp
        dice[3][1] = dice[1][3]
    elif dir == 1:
        tmp = dice[1][3]
        for i in range(3,0,-1):
            dice[1][i] = dice[1][i-dy]
        dice[1][0] = tmp
        dice[3][1] = dice[1][3]

    # 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면,
    # 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
    if grid[nx][ny] == 0:
        # print('11111111111')
        grid[nx][ny] = dice[1][3]

    # 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며,
    # 칸에 쓰여 있는 수는 0이 된다.
    elif grid[nx][ny] != 0:
        # print('2222222222')
        dice[1][3] = grid[nx][ny]
        dice[3][1] = grid[nx][ny]
        grid[nx][ny] = 0

    global x, y
    x = nx
    y = ny
    return True

# rotate([x,y],4)

# get_top()
# print(x, y)
# print(*dice, sep='\n')
# print(*grid, sep='\n')
# 3:남 col[1]+1, 4:북 col[1]-1
# 1:동 row[1]+1, 2:서 col[1]-1
for order in orders:
    # print('------------')
    if rotate([x,y],order):
       get_top()
    # print(f"dir:{order}")
    # print(x,y)
    # print(*dice,sep='\n')
    # print(*grid, sep='\n')

