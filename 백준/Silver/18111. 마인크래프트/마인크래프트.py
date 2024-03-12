import sys
input = sys.stdin.readline

N,M,B = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
# 1번 작업은 2초가 걸리며, 2번 작업은 1초
# 인벤토리에는 B개의 블록이 들어 있다.
# 땅의 높이는 256블록을 초과할 수 없으며, 음수가 될 수 없다.

times = []

cnt = 0
for i in range(N):
    for j in range(M):
        cnt += grid[i][j]
size = N*M

for height in range(257):
    if cnt + B < size*height:
        break

    time = 0
    block = B
    for i in range(N):
        for j in range(M):
            if grid[i][j] > height:
                time += (grid[i][j] - height) * 2
            elif grid[i][j] < height:
                time += height - grid[i][j]
    times.append((time,height))


times.sort(key=lambda x:-x[0])
print(times[-1][0],times[-1][1])
