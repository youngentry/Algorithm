import sys
from collections import deque
input = sys.stdin.readline


N,M,K = map(int,input().split())
trees = [[deque() for _ in range(N)] for _ in range(N)]
ground = [list(map(int,input().split())) for _ in range(N)]
energy = [[5]*N for _ in range(N)]
for _ in range(M):
    tx,ty,tage = map(int,input().split())
    trees[tx-1][ty-1].append(tage)


year = 0
while year < K:
    year += 1
    # 봄
    breedings = set()
    for i in range(N):
        for j in range(N):
            if trees[i][j]: # 나무가 있다면
                dead_tree = 0
                tmp_trees = deque()
                for age in trees[i][j]:
                    if energy[i][j] >= age: # 양분이 있다면
                        energy[i][j] -= age
                        tmp_trees.append(age+1)
                        if (age+1)%5==0:
                            breedings.add((i,j))
                    else: # 양분이 없다면
                        dead_tree += age//2
                trees[i][j] = tmp_trees
                # 여름
                energy[i][j] += dead_tree # 나무가 토양에 양분으로 추가 됨
            # 겨울
            energy[i][j] += ground[i][j]

    # 가을
    directions = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]


    for i,j in breedings: # 생장나무좌표
        for t in trees[i][j]: # 나무들
            if t%5==0: # 생장가능하면
                for di,dj in directions:
                    ni,nj = i+di,j+dj
                    if 0<=ni<N and 0<=nj<N:
                        trees[ni][nj].appendleft(1)

result = 0
for i in range(N):
    for j in range(N):
        result += len(trees[i][j])

print(result)