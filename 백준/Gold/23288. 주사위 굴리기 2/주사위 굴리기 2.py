import sys
from collections import deque

n,m,k = map(int,input().split())
wall = [[0]*(m+2)]
grid = wall+ [[0]+ list(map(int,input().split())) +[0] for _ in range(n)] +wall

dice = [
    [0,2,0,0], #      2:북
    [4,1,3,6], # 4:서 1:상 3:동 6:하
    [0,5,0,0], #      5:남
    [0,6,0,0], #      6:하
]

# 1) 가장 처음에 주사위의 이동 방향은 동쪽

# 2) 점수를 얻는 조건은 밟은 지점에서 bfs로 같은 숫자를 탐색하면 됨


# 3) 주사위 이동 구현
# 주사위가 이동 방향으로 한 칸 굴러간다.
def move_dice(ord):
    # 북쪽으로
    if ord == 0:
        dice[0][1],dice[1][1],dice[2][1],dice[3][1],dice[1][3] = \
        dice[1][1],dice[2][1],dice[3][1],dice[0][1],dice[0][1]
    # 동쪽으로
    if ord == 1:
        dice[1][0],dice[1][1],dice[1][2],dice[1][3],dice[3][1] = \
        dice[1][3],dice[1][0],dice[1][1],dice[1][2],dice[1][2]
    # 남쪽으로
    if ord == 2:
        dice[0][1],dice[1][1],dice[2][1],dice[3][1],dice[1][3] = \
        dice[3][1],dice[0][1],dice[1][1],dice[2][1],dice[2][1]
    # 서쪽으로
    if ord == 3:
        dice[1][0],dice[1][1],dice[1][2],dice[1][3],dice[3][1] = \
        dice[1][1],dice[1][2],dice[1][3],dice[1][0],dice[1][0]

def get_dice_bot():
    return dice[1][3]

directions = [[-1,0],[0,1],[1,0],[0,-1]]
def turn_dice(x,y,bot_num, ord):
    # print(bot_num,grid[x][y])
    if bot_num == grid[x][y]:
        return ord
    if bot_num > grid[x][y]:
        return (ord+1)%4
    if bot_num < grid[x][y]:
        return (ord-1)%4

def bfs(start):
    sx,sy = start[0],start[1]
    restore_pos = [[sx,sy]]
    queue = deque([[sx,sy]])
    bot_num = grid[sx][sy]
    score_sum = grid[sx][sy]
    grid[sx][sy] = 0
    while queue:
        x,y = queue.popleft()
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            if grid[nx][ny] != 0 and grid[nx][ny]==bot_num:
                restore_pos.append([nx,ny])
                score_sum += grid[nx][ny]
                grid[nx][ny] = 0
                queue.append([nx,ny])

    # 숫자 복원
    for rest_x,rest_y in restore_pos:
        grid[rest_x][rest_y] = bot_num
    return score_sum

# 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
# 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.
# 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정한다.
# A > B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
# A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
# A = B인 경우 이동 방향에 변화는 없다.

dice_x, dice_y = 1,1
move_count = 0
ord = 1 # 동쪽에서 시작
total_score = 0
while move_count < k:
    move_count += 1
    # print(*dice,sep='\n')
    # print(dice_x,dice_y,ord,'bbbbb')
    nx,ny = dice_x+directions[ord][0], dice_y+directions[ord][1]
    # 벽을 마주했다면 반대로 후진
    if grid[nx][ny] == 0:
        dice_x,dice_y = dice_x+directions[(ord+2)%4][0], dice_y+directions[(ord+2)%4][1]
        ord = (ord+2)%4
        move_dice(ord)
        ord = turn_dice(dice_x,dice_y,get_dice_bot(),ord)

    # 갈 수 있다면 그대로 전진
    else:
        dice_x,dice_y = nx,ny
        move_dice(ord)
        ord = turn_dice(dice_x,dice_y,get_dice_bot(),ord)

    # print(dice_x,dice_y,ord,'aaaaa')

    # 방향대로 도면 이동
    score = bfs([dice_x,dice_y])
    total_score += score

print(total_score)