import sys
input = sys.stdin.readline

def rotate(N, M, R):
    grid_size = min(N, M) // 2
    for _ in range(R):
        for size in range(grid_size):
            top_left = grid[size][size]

            for j in range(size, M - size - 1):
                grid[size][j] = grid[size][j + 1]
            for i in range(size, N - size - 1):
                grid[i][M - size - 1] = grid[i + 1][M - size - 1]
            for j in range(M - size - 1, size, -1):
                grid[N - size - 1][j] = grid[N - size - 1][j - 1]
            for i in range(N - size - 1, size, -1):
                grid[i][size] = grid[i - 1][size]

            grid[size + 1][size] = top_left


N,M,R = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
rotate(N,M,R)

for arr in grid:
    print(" ".join(map(str,arr)))