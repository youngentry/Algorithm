import sys
input = sys.stdin.readline
from collections import deque

dirs = ((-1,0),(0,1),(1,0),(0,-1))
def bfs(sx,sy):
    global is_finish

    q.append((sx,sy))
    target = grid[sx][sy]
    while q:
        x,y = q.popleft()
        for dx,dy in dirs:
            nx,ny = dx+x, dy+y
            if 0<=nx<N and 0<=ny<M and grid[nx][ny] != 3:
                if grid[nx][ny] == 0:
                    grid[nx][ny] = target
                    q.append((nx,ny))
                elif grid[nx][ny] == target:
                    continue
                else:
                    is_finish = True
                    break

def bfs2(sx,sy,target):
    global is_finish

    q.append((sx,sy))
    grid[sx][sy] = target
    while q and not is_finish:
        x,y = q.popleft()
        for dx,dy in dirs:
            nx,ny = dx+x, dy+y
            if 0<=nx<N and 0<=ny<M:
                if grid[nx][ny] != 3:
                    if (target == 1 and grid[nx][ny] == 2) or (target == 2 and grid[nx][ny] == 1):
                        is_finish = True
                        break

                    if grid[nx][ny] == 0:
                        grid[nx][ny] = target
                        q.append((nx,ny))
                    elif grid[nx][ny] == target:
                        continue
                else:
                    next_set.add((nx,ny,target))


N, M = map(int,input().split())
grid = []
l1 = None
l2 = None
for i in range(N):
    row = list(input().strip())
    tmp_row = []
    for j in range(M):
        if row[j] == "L":
            if not l1:
                l1 = (i,j)
                tmp_row.append(1)
            else:
                l2 = (i,j)
                tmp_row.append(2)
        elif row[j] == ".":
            tmp_row.append(0)
        elif row[j] == "X":
            tmp_row.append(3)
    grid.append(tmp_row)


is_finish = False

# 0:호수 1:백조 2:백조 3:얼음
q = deque()
bfs(l1[0],l1[1])
bfs(l2[0],l2[1])

day = 0
if is_finish:
    print(day)
else:
    # 가장자리 찾기
    border_set = set()
    for i in range(N):
        for j in range(M):
            if grid[i][j] != 3:
                for di, dj in dirs:
                    ni, nj = di + i, dj + j
                    if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] == 3:
                        border_set.add((ni,nj,grid[i][j]))

    day = 0
    while not is_finish:
        next_set = set() # 다음 시행
        day += 1
        while border_set and not is_finish:
            x,y,num = border_set.pop()

            grid[x][y] = num
            for dx, dy in dirs:
                nx, ny = dx + x, dy + y
                if 0 <= nx < N and 0 <= ny < M:
                    if grid[nx][ny] == 1:
                        grid[x][y] = 1
                        bfs2(x,y,1)
                        break
                    elif grid[nx][ny] == 2:
                        grid[x][y] = 2
                        bfs2(x,y,2)
                        break

            for dx, dy in dirs:
                nx, ny = dx + x, dy + y
                if 0 <= nx < N and 0 <= ny < M:
                    # 다른 백조 만나면 종료
                    if (num==1 and grid[nx][ny]==2) or (num==2 and grid[nx][ny]==1):
                        is_finish = True
                        break
                    elif ((num==1 or num==2) and grid[nx][ny]==0):
                        grid[x][y] = num
                        bfs2(nx,ny,num)
                    elif grid[nx][ny] == 3:
                        next_set.add((nx, ny, num))

        border_set = next_set
        
    print(day)