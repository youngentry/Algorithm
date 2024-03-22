dirs = ((-1,0),(0,1),(1,0),(0,-1))

def dfs(y,x,path):
    # 기저조건: 7자리
    if len(path) == 7:
        # 현재까지의 경로를 저장
        result.add(path)
        return

    for dy,dx in dirs:
        ny,nx = y+dy, x+dx

        # 범위 밖으로 넘어가면 pass
        if ny<0 or ny>=4 or nx<0 or nx>=4:
            continue

        dfs(ny,nx,path + maps[ny][nx])


T = int(input())
for tc in range(1, T+1):
    # 격자판 저장
    # 갈 때 마다 경로를 더하기위해서 문자열로 저장
    maps = [input().split() for _ in range(4)]
    # 중복을 제거하기 위해 set 사용
    result = set()

    # 시작 지점
    for i in range(4):
        for j in range(4):
            dfs(i, j, maps[i][j])

    print(f'#{tc} {len(result)}')