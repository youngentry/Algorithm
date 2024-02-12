import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

# 입력 받기
n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
copied_maps = deepcopy(maps)
# print(*maps,sep='\n')

# 벽 3개를 세워야 함
# 0:빈칸, 1:벽, 2:바이러스

# 1. 경우의 수가 적으므로 완탐으로 접근
# 2. 벽을 세 개 세웠다면 바이러스를 퍼뜨린 뒤의 결과를 max_safe에 저장
# 그렇다면 벽을 어떻게 모든 경우에 세우냐가 포인트
# 0이 될 수 있는 모든 조합을 생성함
# 그 중 3개를 뽑음
# 모든 조합에 대해 바이러스 체크를 함
# 체크한 뒤엔 원래대로 복원함


blanks = [] # 벽 조합
virus = [] # 바이러스 위치
for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            blanks.append([i,j])
        if maps[i][j] == 2:
            virus.append([i,j])
combs = list(combinations(blanks,3))

max_safe = 0
directions = [[-1,0],[0,1],[1,0],[0,-1]]
for comb in combs:
    # 벽치기
    for x,y in comb:
        copied_maps[x][y] = 1

    # 바이러스 세팅
    queue = deque(virus)
    while queue:
        x,y = queue.popleft()
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and copied_maps[nx][ny] == 0:
                copied_maps[nx][ny] = 2
                queue.append([nx,ny])

    # 안전영역 탐색
    temp_safe = 0
    for i in range(n):
        for j in range(m):
            if copied_maps[i][j] == 0:
                temp_safe += 1

    # 결과 확인
    max_safe = max(max_safe,temp_safe)

    # map 되돌리기
    for i in range(n):
        for j in range(m):
            copied_maps[i][j] = maps[i][j]

print(max_safe)