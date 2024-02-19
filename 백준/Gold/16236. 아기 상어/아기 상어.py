import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline


def transform(str_int):
    return [int(str_int),0]

def init_grid(arr):
    for i in range(1,N+1):
        for j in range(1,N+1):
            arr[i][j][1] = 0

def find_fish(arr):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if arr[i][j][0] == 9:
                return [i,j]

# 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다
# 자신의 크기보다 작은 물고기만 먹을 수 있다
def bfs(sx,sy,smove):
    init_grid(grid) # 방문 배열 초기화

    queue = deque([[sx,sy,smove]])
    feedable = []
    grid[sx][sy] = [0,1]

    while queue:
        x,y,move = queue.popleft()
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            # 크기가 크지 않고, 방문이 아니라면
            if grid[nx][ny][0] <= size and grid[nx][ny][1] == 0:
                queue.append((nx,ny,move+1)) # 해당 위치로 이동
                grid[nx][ny][1] = 1 # 방문처리

                if grid[nx][ny][0] != 0 and grid[nx][ny][0] < size:
                    feedable.append([nx,ny,move+1])
    return feedable


N = int(input())
wall = [[[999,1]]*(N+2)]
grid = wall+ [[[999,1]]+list(map(transform,input().split()))+[[999,1]] for _ in range(N)] +wall
fish_x,fish_y = find_fish(grid)

directions = [[-1,0],[0,1],[1,0],[0,-1]]

size = 2
need_feed = size
time = 0
while True:
    bfs_result = bfs(fish_x,fish_y,0)
    # 먹을 수 있는 물고기가 없다면 엄마상어 부르기
    if len(bfs_result) == 0:
        break

    # 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다
    if len(bfs_result) == 1:
        feed_x,feed_y,distance = bfs_result.pop()
        grid[feed_x][feed_y] = [9,0]
        fish_x,fish_y = feed_x,feed_y
        time += distance

        # 물고기 크기 조절
        need_feed -= 1
        if need_feed == 0:
            size += 1
            need_feed = size
        continue

    # 짧은 같은 거리가 1마리 이상, 가장 위, 가장 왼쪽 물고기 먹기
    bfs_result.sort(key=lambda x:(x[2],x[0],x[1]))

    feed_x,feed_y,distance = bfs_result[0]
    grid[feed_x][feed_y] = [9,0]
    fish_x,fish_y = feed_x,feed_y

    time += distance

    # 물고기 크기 조절
    need_feed -= 1
    if need_feed == 0:
        size += 1
        need_feed = size

print(time)