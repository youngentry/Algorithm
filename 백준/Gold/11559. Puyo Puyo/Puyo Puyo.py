import sys
from collections import deque
import time
input = sys.stdin.readline
# st = time.time()

def bfs(sx,sy):
    global is_continue

    target = grid[sx][sy]
    q = deque([(sx,sy)])
    v = [grid[i][:] for i in range(row)]
    v[sx][sy] = "."
    cnt = 1
    pos = [(sx,sy)]
    while q:
        x,y = q.popleft()
        for dx,dy in ((-1,0),(0,1),(1,0),(0,-1)):
            nx,ny = x+dx,y+dy
            if 0<=nx<row and 0<=ny<col and v[nx][ny] == target:
                v[nx][ny] = "."
                pos.append((nx,ny))
                cnt += 1
                q.append((nx,ny))
    if len(pos) > 3:
        # print(pos)
        for px, py in pos:
            grid[px][py] = "."
        is_continue = True

row = 12
col = 6
grid = [list(input().strip()) for _ in range(12)]
ans = 0
while True:
    is_continue = False
    # bfs로 4연 이상인 좌표 찾기
    for i in range(row):
        for j in range(col):
            if grid[i][j] != ".":
                bfs(i,j)

    # print(*grid,sep='\n')
    # 빈 자리 끌어 내리기
    for k in range(12):
        for i in range(col):
            for j in range(row-1,0,-1):
                if grid[j-1][i] != "." and grid[j][i] == ".":
                    grid[j][i], grid[j-1][i] = grid[j-1][i], grid[j][i]
#     print('-------------')
#     print(*grid,sep='\n')
#     print('=============')
    if is_continue:
        ans += 1
    else:
        break

print(ans)
# print(time.time() - st)