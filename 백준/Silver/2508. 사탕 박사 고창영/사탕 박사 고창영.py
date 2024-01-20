import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for t_c in range(T):
    input()
    r,c = map(int,input().split())

    # 행렬 만들기
    grid = []
    for _ in range(r):
        grid.append([*input().strip()])

    # 사탕 카운트
    count = 0
    for row in range(r):
        for col in range(c):
            if col<c-2 and grid[row][col] + grid[row][col+1] + grid[row][col+2] == ">o<":
                # print(grid[row][col] + grid[row][col+1] + grid[row][col+2])
                count += 1
            elif row<r-2 and grid[row][col] + grid[row+1][col] + grid[row+2][col] == "vo^":
                # print(grid[row][col] + grid[row+1][col] + grid[row+2][col])
                count += 1

    print(count)

