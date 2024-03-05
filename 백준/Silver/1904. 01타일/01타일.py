import sys
input = sys.stdin.readline

N = int(input().strip())

dp = [0] * (1000001)
dp[1] = 1
dp[2] = 2

if N == 1:
    print(1)
else:
    for i in range(3,N+1):
        dp[i] = (dp[i-2] + dp[i-1])%15746

    print(dp[N])