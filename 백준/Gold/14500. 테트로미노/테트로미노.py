import sys
n,m = map(int,input().split())

possibles = [
    [[0,0],[0,1],[0,2],[0,3]],   # 4가로
    [[0,0],[1,0],[2,0],[3,0]],   # 4세로
    [[0,0],[0,1],[1,0],[1,1]],   # 사각
    [[0,0],[1,0],[2,0],[2,1]],   # L 1
    [[0,0],[0,1],[0,2],[1,0]],   # L 2
    [[0,0],[0,1],[1,1],[2,1]],   # L 3
    [[0,2],[1,0],[1,1],[1,2]],   # L 4
    [[0,1],[1,0],[1,1],[1,2]],   # ㅗ 1
    [[0,0],[1,0],[2,0],[1,1]],   # ㅗ 2
    [[0,0],[0,1],[0,2],[1,1]],   # ㅗ 3
    [[0,1],[1,0],[1,1],[2,1]],   # ㅗ 4
    [[0,0],[1,0],[1,1],[2,1]],   # ㄹ 1
    [[0,1],[0,2],[1,0],[1,1]],   # ㄹ 2
    [[0,0],[0,1],[1,1],[1,2]],   # ㄹ 3
    [[0,1],[1,0],[1,1],[2,0]],   # ㄹ 4
    [[0,0],[1,0],[1,1],[1,2]],   # ㄱ 1
    [[0,0],[0,1],[1,0],[2,0]],   # ㄱ 2
    [[0,0],[0,1],[0,2],[1,2]],   # ㄱ 3
    [[0,1],[1,1],[2,0],[2,1]],   # ㄱ 4
]

grid = [list(map(int,input().split())) for _ in range(n)]

max_count = 0
for i in range(n):
    for j in range(m):
        for possible in possibles:
            block_count = 0
            for di,dj in possible:
                if i+di<n and j+dj<m:
                    block_count += grid[i+di][j+dj]
                else:
                    block_count = 0
                    break
            max_count = max(max_count,block_count)

print(max_count)