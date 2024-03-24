import sys
sys.setrecursionlimit(100000)  # 재귀 깊이 제한 설정
from collections import deque
import heapq
import time
input = sys.stdin.readline  # 입력 속도를 높이기 위해 sys.stdin.readline 사용
from math import floor

# st = time.time()
# ======================================
dirs = ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1))
def BFS(sx,sy,mx_size):
    q = deque([(sx,sy,grid[sx][sy])])
    v = [[0]*M for _ in range(N)]

    while q:
        x,y,cur = q.popleft()
        if cur in check:
            check[cur] += 1

        if len(cur) == mx_size:
            continue

        for dx,dy in dirs:
            nx,ny = (x+dx+N)%N, (y+dy+M)%M
            if 0<=nx<N and 0<=ny<M:
                q.append((nx,ny,cur+grid[nx][ny]))


N,M,K = map(int,input().split())
grid = [list(input().strip()) for _ in range(N)]

check = {}
mx_size = 0
for i in range(K):
    word = input().strip()
    check[word] = 0
    mx_size = max(len(word),mx_size)

for i in range(N):
    for j in range(M):
        like = input().strip()
        BFS(i,j,mx_size)

for value in check.values():
    print(value)
# ======================================
# print(time.time() - st)
