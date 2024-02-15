import sys
input = sys.stdin.readline
from copy import deepcopy

#  좌표 평면의 x축은 → 방향, y축은 ↓ 방향

# 0세대 드래곤 커브는 아래 그림과 같은 길이가 1인 선분
# 시작 방향은 오른쪽

# 1세대 드래곤 커브는 
# 0세대 드래곤 커브를 끝 점을 기준으로 시계 방향으로 90도 회전시킨 다음 
# 0세대 드래곤 커브의 끝 점에 붙인 것

# 즉, K(K > 1)세대 드래곤 커브는 K-1세대 드래곤 커브를 
# 끝 점을 기준으로 90도 시계 방향 회전 시킨 다음, 그것을 끝 점에 붙인 것

n = int(input())
dragons = [list(map(int,input().split())) for _ in range(n)]
# x,y시작점 d방향, g세대

# print(n,dragons)
grid = [[0]*101 for _ in range(101)]

# print(*grid,sep='\n')

def turn(arr):
    tmp_arr = deepcopy(arr)
    cx,cy = tmp_arr[-1]

    for i in range(len(tmp_arr)):
        tmp_arr[i][0] -= cx
        tmp_arr[i][1] -= cy

    for i in range(len(tmp_arr)):
        tmp_arr[i][0],tmp_arr[i][1] = tmp_arr[i][1],-tmp_arr[i][0]
        
    for i in range(len(tmp_arr)):
        tmp_arr[i][0] += cx
        tmp_arr[i][1] += cy

    return list(reversed(tmp_arr))[1:]
    

def curve(g,arr,count):
    global grid
    if count == g:
        curved_arr = arr 
        # print(curved_arr,"curved_arrcurved_arrcurved_arr")
        for curv_x,curv_y in curved_arr:
            grid[curv_x][curv_y] = 1
        return 
    
    new_arr = [*arr, *turn(arr)]

    # print(new_arr)
    curve(g,new_arr,count+1)

# 0:[0,1] 1:[0,-1] 2:[0,-1] 3:[1,0] 
directions = [[0,1],[-1,0],[0,-1],[1,0]] 
results = []
for i in range(n):
    y,x,d,g = dragons[i]
    dx,dy = directions[d]
    start_arr = [[x,y],[x+dx,y+dy]]
    curve(g,start_arr,0)

    # print(*grid,sep='\n')
    
for i in range(101):
    grid[i] += [0]
grid += [[0]*(101+1)]
# print(*grid,sep='\n')

count = 0
for i in range(101):
    for j in range(101):
        if  grid[i][j] == 1 and \
            grid[i+1][j] == 1 and \
            grid[i][j+1] == 1 and \
            grid[i+1][j+1] == 1:
            count += 1

print(count)