import sys
input = sys.stdin.readline
from collections import deque


N,M,P = map(int,input().split())
p_moves =[0] + list(map(int,input().split()))
grid = []
starts = [[] for _ in range(P+1)]
for i in range(N):
    row = list(input().strip())
    tmp_row = []
    for j in range(M):
        if row[j].isdecimal():
            num = int(row[j])
            starts[num].append((i,j,num,p_moves[num]))
            tmp_row.append(num)
        else:
            tmp_row.append(row[j])
    grid.append(tmp_row)

q = deque()
for start in starts[1:]:
    for pos in start:
        q.append(pos)
tmp_move_q = deque()
while q:
    bx,by,bnum,brm = q.popleft()
    while q and q[0][2] == bnum:
        tmp_move_q.append(q.popleft())
    tmp_move_q.append((bx,by,bnum,brm))

    # remain_move만큼 bfs를 돌림
    while tmp_move_q:
        x,y,num,remain_move = tmp_move_q.popleft()
        remain_move -= 1
        for dx,dy in ((-1,0),(0,1),(1,0),(0,-1)):
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<M and grid[nx][ny]==".":
                if remain_move == 0:
                    q.append((nx,ny,num,p_moves[num]))
                else:
                    tmp_move_q.append((nx,ny,num,remain_move))
                grid[nx][ny] = num

counts = [0]*(P+1)
for i in range(N):
    for j in range(M):
        if type(grid[i][j]) == int:
            counts[int(grid[i][j])] += 1
print(*counts[1:])