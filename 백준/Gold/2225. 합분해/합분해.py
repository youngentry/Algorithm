import sys
input = sys.stdin.readline

N,M = map(int,input().split())
size = 200
dp = [[i]*(size+1) for i in range((size+1))]

for i in range(1,size+1):
    for j in range(1,size+1):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]

print(dp[M][N-1]%1000000000)

# 1 1  1  1  1
# 2 3  4  5  6
# 3 6 10 15 21

