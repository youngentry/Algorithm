import sys
input = sys.stdin.readline 

# N×N인 체스판
# 사용하는 말의 개수는 K개
N,K = map(int,input().split())
wall = [[2]*(N+2)]
# 체스판
grid = wall+[[2]+list(map(int,input().split()))+[2] for _ in range(N)]+wall
# 말 위치
big_wall = [[[99,99]]*(N+2)]
chesses = big_wall+[[[99,99]]+[[] for _ in range(N)]+[[99,99]] for _ in range(N)]+big_wall
for i in range(1,K+1):
    sx,sy,sdir = map(int,input().split())
    chesses[sx][sy] = [[i,sdir]]
directions = [[0,1],[0,-1],[-1,0],[1,0]]

# 0:흰색, 1:빨간색, 2:파란색
# 하나의 말 위에 다른 말을 올릴 수 있다
# 턴 한 번은 1번 말부터 K번 말까지 순서대로 이동시키는 것
# 한 말이 이동할 때 위에 올려져 있는 말도 함께 이동한다
is_finish = False
def move(level,x,y,dir):
    global is_finish

    dir = dir - 1
    nx,ny = x+directions[dir][0],y+directions[dir][1]
    stacks = chesses[x][y][level:]
    remains = chesses[x][y][:level]

    # 흰색인 경우에는 그 칸으로 이동한다
    # 이동하려는 칸에 말이 이미 있는 경우에는 가장 위에 A번 말을 올려놓는다
    # A번 말의 위에 다른 말이 있는 경우에는 A번 말과 위에 있는 모든 말이 이동한다
    # 예를 들어, A, B, C로 쌓여있고, 
    # 이동하려는 칸에 D, E가 있는 경우에는 A번 말이 이동한 후에는 D, E, A, B, C가 된다
    # 0: 흰색
    if  grid[nx][ny] == 0:
        chesses[nx][ny] += stacks
        chesses[x][y] = remains

    # 빨간색인 경우에는 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다
    # A, B, C가 이동하고, 이동하려는 칸에 말이 없는 경우에는 C, B, A가 된다
    # A, D, F, G가 이동하고, 이동하려는 칸에 말이 E, C, B로 있는 경우에는 E, C, B, G, F, D, A가 된다
    # 1: 빨간색
    elif  grid[nx][ny] == 1:
        chesses[nx][ny] += stacks[::-1]
        chesses[x][y] = remains

    # 2: 파란색
    elif grid[nx][ny] == 2:
        # A번 말의 이동 방향을 반대로 하고 한 칸 이동한다.
        if stacks[0][1] == 1:
            stacks[0][1] = 2
        elif stacks[0][1] == 2:
            stacks[0][1] = 1
        elif stacks[0][1] == 3:
            stacks[0][1] = 4
        elif stacks[0][1] == 4:
            stacks[0][1] = 3
        nx,ny = x+directions[stacks[0][1]-1][0],y+directions[stacks[0][1]-1][1]
        # 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다
        # 체스판을 벗어나는 경우에는 파란색과 같은 경우이다.
        if grid[nx][ny] == 2:
            if len(chesses[x][y])>=4:
                is_finish = True
            return
        elif  grid[nx][ny] == 1:
            chesses[nx][ny] += stacks[::-1]
            chesses[x][y] = remains
        elif  grid[nx][ny] == 0:
            chesses[nx][ny] += stacks
            chesses[x][y] = remains

    # 턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료된다
    if len(chesses[nx][ny])>=4:
        is_finish = True

# 방향정보 1~4 순서대로 →, ←, ↑, ↓
turn = 0
while turn < 1000:
    turn += 1
    for k in range(1,K+1):
        is_found = False
        for i in range(1,N+1):
            for j in range(1,N+1):
                for p in range(len(chesses[i][j])):
                    # k번 체스를 찾았다면
                    if chesses[i][j][p][0] == k:
                        move(p,i,j,chesses[i][j][p][1])
                        is_found = True
                        break
                if is_found or is_finish:
                    break
            if is_found or is_finish:
                break

    if is_finish:
        print(turn)
        break

if not is_finish:
    print(-1)