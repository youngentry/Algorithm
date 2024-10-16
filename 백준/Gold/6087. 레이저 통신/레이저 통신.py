import sys
from _collections import deque

input = sys.stdin.readline

W,H = map(int,input().split())

grid = [list(list(input().strip())) for _ in range(H)]


q = deque([])


for i in range(H):
    for j in range(W):
        if grid[i][j] == '.':
            grid[i][j] = 99999
# print(*grid,sep='\n')

start_cnt = 0

start_pos = None
end_pos = None
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'C':
            if start_cnt == 1:
                grid[i][j] = 999999
                end_pos = [i,j]
                continue
            grid[i][j] = 0
            q.append((i,j,0,0))
            q.append((i,j,0,1))
            q.append((i,j,0,2))
            q.append((i,j,0,3))
            start_cnt = 1
            start_pos = [i,j]
# print(*grid,sep='\n')

dirs = ((-1,0),(0,1),(1,0),(0,-1))

def go_straight(x,y,c,d):
    # print(*grid,sep='\n')
    # print('---------------------------')
    bx,by = x+dirs[d][0], y+dirs[d][1]
#     print('straight','bx,by', bx, by, 'c,d', c, d)
#     print(q)
    if 0<=bx<H and 0<=by<W and grid[bx][by] != '*' and grid[bx][by] >= c:
#         print('in','bx,by',bx,by,'c,d',c,d)
        grid[bx][by] = c
        go_straight(bx,by,c,d)

    nx, ny = x + dirs[(d+1)%4][0], y + dirs[(d+1)%4][1]
    if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != '*' and grid[nx][ny] > c + 1:
        grid[nx][ny] = c + 1
        q.append((nx, ny, c + 1, (d+1)%4))

    nx, ny = x + dirs[(d-1)%4][0], y + dirs[(d-1)%4][1]
#     print(nx,ny, c+1, (d+1)%4)
    if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != '*' and grid[nx][ny] > c + 1:
        grid[nx][ny] = c + 1
        q.append((nx, ny, c + 1, (d-1)%4))




while q:
    x,y,c,d = q.popleft()

    # 해당 방향으로 계속해서 날리기
    go_straight(x,y,c,d)
#     print('====================')


print(grid[end_pos[0]][end_pos[1]])
