from _collections import deque

N,R,D,X,Y = map(int,input().split())

# 1. 적과 닿아있는 타워, 닿아있지 않은 타워 분류
# 2. 적과 닿아있는 타워에서 시작하여 닿아있지 않은 타워 줄기를 연결
# 3. 타워 줄기의 차수에 따라 결과치 합산
#  3-1. 타워 줄기는 BFS로 구하기

near_towers = []
away_towers = []

for i in range(N):
    x,y = map(int,input().split())
    if ((X-x)**2 + (Y-y)**2) <= R**2:
        near_towers.append((x,y,0))
    else:
        away_towers.append((x,y))

# print(near_towers)
# print(away_towers)

result = D * len(near_towers)
visited = [0] * len(away_towers)

cur_towers = deque([*near_towers])
while cur_towers:
    x,y,degree = cur_towers.popleft()

    for i in range(len(away_towers)-1,-1,-1):
        if visited[i]:
            continue

        ax,ay = away_towers[i]
#         print(x,ax,y,ay,(x - ax) ** 2 + (y - ay) ** 2,R**2)
        if ((x - ax) ** 2 + (y - ay) ** 2) <= R**2:
            visited[i] = degree+1
            cur_towers.append((*away_towers[i],degree+1))

# print(visited)
for i in range(len(visited)):
    if visited[i]:
        result += D * (1/2 ** (visited[i]))
#         print(D * (1/2 ** (visited[i])))
print(result)