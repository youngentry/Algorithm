import sys
input = sys.stdin.readline 

N,K = map(int,input().split())
numbers = [int(input().strip()) for _ in range(N)]

dp = [987654321]*(100000+1)
# 0과 각 num은 1가지 경우의 수로 만들어 진다.
dp[0] = 1
for num in numbers:
    dp[num] = 1

for i in range(1, K+1):
    for num in numbers:
        if i>=num:
            # i번째 경우와, dp[i-num]번째 경우에 +1 한 값과 비교하여 작은 값 선택
            dp[i] = min(dp[i],dp[i-num]+1)

if dp[K] == 987654321:
    print(-1)
else:
    print(dp[K])
