import sys
from collections import deque
input = sys.stdin.readline

def find_outer_cheese():
    q = deque([(0,0)])
    v[0][0] = 9
    outer_cheese = set()
    while q:
        x,y = q.popleft()
        for dx,dy in dirs:
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<M:
                if v[nx][ny] == 0:
                    v[nx][ny] = 9
                    q.append((nx,ny))
                elif v[nx][ny] == 1:
                    outer_cheese.add((nx,ny))
                    v[nx][ny] = 9
    return outer_cheese


N,M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
cheeses = set()
cheeses_cnt = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            cheeses_cnt += 1
            cheeses.add((i,j))

dirs = ((-1,0),(0,1),(1,0),(0,-1))
time = 0
last_cheese_cnt = None

while cheeses_cnt > 0:
    last_cheese_cnt = cheeses_cnt
    melt_cheese = []
    v = [grid[i][:] for i in range(N)]
    melt_cheese = find_outer_cheese()

    for tup in melt_cheese:
        x,y = tup
        grid[x][y] = 0
        cheeses.remove(tup)
        cheeses_cnt -= 1
    time += 1
    if cheeses_cnt == 0:
        break

print(time)
print(last_cheese_cnt)