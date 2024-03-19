import sys

def dfs(n):
    global N
    global mx

    # 전부 시도해 봤다면 종료
    if n == N:
        tmp_cnt = 0
        for endu, wei in eggs:
            if endu <= 0:
                tmp_cnt += 1
            mx = max(mx, tmp_cnt)
        return


    # 들고 있는 계란이 깨져있다면 다음 계란 확인
    if eggs[n][0] <= 0:
        dfs(n+1)
        return

    for j in range(N):
        # 마지막 선택지까지 시도해본 경우
        if n == N - 1 and j == N - 1:
            dfs(n + 1)
            return

        # 자기 자신은 칠 수 없음
        if n == j:
            continue

        # 치려는 계란이 깨져 있다면 다음 계란 확인
        if eggs[j][0] <= 0:
            # 칠 계란이 하나도 없다면 다음 계란 확인
            if j==N-1:
                dfs(n+1)
            continue

        eggs[j][0] -= eggs[n][1]
        eggs[n][0] -= eggs[j][1]
        dfs(n+1)
        eggs[j][0] += eggs[n][1]
        eggs[n][0] += eggs[j][1]



N = int(input())
eggs = [list(map(int,input().split())) for _ in range(N)]
mx = 0
dfs(0)
print(mx)