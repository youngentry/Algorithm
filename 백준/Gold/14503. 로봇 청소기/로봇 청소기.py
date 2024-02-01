import sys

input = sys.stdin.readline

global grid
global directions
global on_running
global count

on_running = True
directions = [[-1,0],[0,1],[1,0],[0,-1]]
count = 0

grid = [] # 1:벽, 0:청소안된 빈칸
n,m = map(int,input().split())
r,c,d = map(int,input().split()) #d: 0북, 1동, 2남, 3서
pos_x, pos_y = r,c

for _ in range(n):
    grid.append(list(map(int,input().split())))

def clean_up(x,y):
    global grid
    global count
    if grid[x][y] == 0:
        grid[x][y] = 9
        count+=1

def get_is_clean(x,y):
    global grid
    global directions
    is_clean = True
    for dx, dy in directions:
        # print(x,dx,y,dy,grid[x+dx][y+dy],"좌표")
        if grid[x+dx][y+dy] == 0:
            is_clean = False
    return is_clean

def back(x,y,d):
    global grid
    global directions
    if grid[x-directions[d][0]][y-directions[d][1]] == 1:
        return stop()
    else:
        return [x-directions[d][0],y-directions[d][1]]
    
def stop():
    global on_running
    on_running = False
    return [0,0]

def turn(d):
    if d-1 < 0:
        return 3
    else:
        return d-1

def go(x,y,d):
    global grid
    global directions
    if grid[x+directions[d][0]][y+directions[d][1]] == 0:
        return [x+directions[d][0],y+directions[d][1]]
    else:
        return [x,y]

while on_running:
    # print(*grid,sep='\n')
    # print(pos_x,pos_y,count,d)
    clean_up(pos_x,pos_y)
    is_clean = get_is_clean(pos_x,pos_y)
    if is_clean:
        pos_x,pos_y = back(pos_x,pos_y,d)
    else:
        d = turn(d)
        pos_x,pos_y = go(pos_x,pos_y,d)

print(count)

# 그래서 몇 칸 청소하니?
# 1. 칸청소
# 2. 청소되지 않은 주변빈칸 없으면 후진, 후진 못하면 작동중지
# 3. 청소되지 않은 빈칸이 있으면 반시계로 90도 회전
# 4. 청소되지 않은 빈칸을 바라보았다면 한 칸 전진