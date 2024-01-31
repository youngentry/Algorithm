import sys
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

n,m = map(int,input().split())
grid = []
chicken_coord = [] # 치킨집 좌표 저장
# 지도 생성
for i in range(n):
    line = list(map(int,input().split()))
    # 치킨집 추가
    for j in range(n):
        if line[j] == 2:
            chicken_coord.append([i,j])
            line[j] = 0 # 치킨집 일단 제외
    grid.append(line)

# 치킨집 조합 생성
combs = list(combinations(chicken_coord,m))

# 폐업 시뮬레이션
results = []
for chickens in combs:
    dists = []
    # 폐업 시뮬레이션 지도 설정
    copied_grid = deepcopy(grid)
    for x,y in chickens:
        copied_grid[x][y] = 2 # 치킨집 위치 설정

    # 모든 1에 대해 2까지, 각각의 최단 거리 구하기
    for i in range(n):
        for j in range(n):
            if copied_grid[i][j] == 1:
                min_dist = 987654321
                for k in range(n):
                    for l in range(n):
                        if copied_grid[k][l] == 2:
                            min_dist = min(min_dist, abs(i-k)+abs(j-l))
                dists.append(min_dist)

    # 결과에 치킨거리 추가
    results.append(sum(dists))

# 모든 치킨 거리 중 가작 작은 값 반환
print(min(results))