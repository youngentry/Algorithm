import sys
from _collections import deque

N = int(input())

grid = [list(map(int,input().split())) for _ in range(N)]
#
# print(*grid,sep='\n')

width = N

while width > 1:
    width //= 2

    temp_grid = [[] for _ in range(width)]

    for i in range(width):
        for j in range(width):
            temp_grid[i].append(sorted([grid[i*2][j*2],
                                 grid[i*2+1][j*2],
                                 grid[i*2][j*2+1],
                                 grid[i*2+1][j*2+1]])[2])

    grid = temp_grid

# print(*grid,sep='\n')

print(grid[0][0])