import sys

input = sys.stdin.readline

n = int(input())
grid = [[0]*n for _ in range(n)]

for i in range(n):
    line = list(map(int,input().split()))
    for j in range(len(line)):
        grid[i][j] = line[j]

for i in range(1,n):
    for j in range(n):
        grid[i][j] = max(grid[i][j]+ grid[i-1][j] ,grid[i][j] + grid[i-1][j-1])

print(max(grid[-1]))