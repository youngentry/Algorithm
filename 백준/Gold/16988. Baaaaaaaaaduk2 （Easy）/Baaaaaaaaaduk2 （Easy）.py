import sys
from collections import deque
input = sys.stdin.readline


N,M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

def bfs(sx,sy,v):
    q = deque([(sx,sy)])

    # 돌 한개가 갇힌 케이스라면 바로 종료
    one_cnt = 0
    for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        nx, ny = sx + dx, sy + dy
        if 0 <= nx < N and 0 <= ny < M:
            if v[nx][ny] == 1 and grid[nx][ny] != 2:
                one_cnt += 1
        else:
            one_cnt += 1
    if one_cnt == 4:
        return 1

    # 연결된 군집 중에서 0과 맞닿은 영역이 있다면 bad
    cnt = 0
    is_bad = False
    while q:
        x,y = q.popleft()
        for dx,dy in ((-1,0),(0,1),(1,0),(0,-1)):
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<M:
                if v[nx][ny] == 0:
                    is_bad = True
                    break
                elif v[nx][ny] == 2:
                    v[nx][ny] = 1
                    cnt += 1
                    q.append((nx,ny))
    if is_bad:
        return 0
    else:
        return cnt


def dfs(row, col, cnt):
    global mx

    if cnt == 0:  # 모든 돌을 놓았을 때
        kill_result = 0
        v = [grid[i][:] for i in range(N)]
        for i in range(N):
            for j in range(M):
                if v[i][j] == 2:
                    kill_result += bfs(i,j,v)
        mx = max(mx,kill_result)
        return

    for i in range(row, N):
        if i == row:
            start_col = col
        else:
            start_col = 0
        for j in range(start_col, M):
            if grid[i][j] != 0:
                continue

            grid[i][j] = 1  # 돌을 놓음
            dfs(i, j, cnt - 1)  # 다음 돌을 놓으러 재귀 호출
            grid[i][j] = 0  # 백트래킹

        col = 0  # 다음 행부터는 첫 열부터 시작해야 하므로 col 초기화

mx = 0
dfs(0, 0, 2)  # 백트래킹 함수 호출
print(mx)