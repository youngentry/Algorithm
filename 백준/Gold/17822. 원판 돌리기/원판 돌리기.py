import sys
from collections import deque 

def bfs(si,sj):
    global is_changed
    global remains

    queue = deque([(si,sj)])
    check_num = circles[si][sj]
    tmp_changed = False # 인접처리한 숫자가 있으면 True로 변환
    while queue:
        x,y = queue.popleft()

        for dx,dy in dirs:
            nx,ny = (x+dx),(y+dy)%M
            # 같은 숫자인 경우 방문처리하고, 0으로 변경
            if 0<=nx<N and 0<=ny<M and v[nx][ny] == 0 \
                and circles[nx][ny] == check_num:
                v[nx][ny] = 1
                circles[nx][ny] = 0
                remains -= 1
                queue.append((nx,ny))
                tmp_changed = True

                
    
    # 숫자가 변했다면 초기 위치도 제거
    if tmp_changed:
        circles[si][sj] = 0
        is_changed = True

# N개원판, M개정수, T번회전
N,M,T = map(int,input().split())
circles = [deque(map(int,input().split())) for _ in range(N)]
# 번호 xi의 배수인 원판을 di방향으로 ki칸 회전 (di가 0이면 시계, 1이면 반시계)
xdk = [list(map(int,input().split())) for _ in range(T)]
remains = N*M
dirs = [[-1,0],[0,1],[1,0],[0,-1]]

for X,D,K in xdk:
    # 번호가 xi의 배수인 원판을 di방향으로 ki칸 회전시킨다
    for xi in range(N):
        if (xi+1)%X == 0:
            for ki in range(K):
                if D == 0: # 시계
                    circles[xi].appendleft(circles[xi].pop())
                elif D == 1: # 반시계
                    circles[xi].append(circles[xi].popleft())

    is_changed = False
    # 인접처리
    v = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if circles[i][j] != 0:
                bfs(i,j)
    
    if not is_changed and remains:
    # 원판에 적힌 수의 평균을 구하고, 
    # 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다
        tmp_sum = 0
        for i in range(N):
            for j in range(M):
                tmp_sum += circles[i][j]
        tmp_sum /= remains

        for i in range(N):
            for j in range(M):
                if circles[i][j] != 0:
                    if circles[i][j] > tmp_sum:
                        circles[i][j] -= 1
                    elif circles[i][j] < tmp_sum:
                        circles[i][j] += 1

ans = 0
for i in range(N):
    for j in range(M):
        ans += circles[i][j]
print(ans)