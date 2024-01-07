N = int(input())

scores = [0] * 301

for i in range(1,N+1):
    scores[i] = int(input())

dp = [0] * 301

dp[1] = scores[1]
dp[2] = scores[1]+scores[2]
dp[3] = max(scores[3]+scores[1], scores[3]+scores[2])

for i in range(4,N+1):
    dp[i] = max(scores[i]+scores[i-1]+dp[i-3] , scores[i]+dp[i-2])

print(dp[N])