target = int(input())

dp = [float('inf') for _ in range(int(target+1))]
dp[1] = 1

# dp 아이디어
# index에 필요한 연산 횟수를 저장한다
# 저장할 때 더 적은 연산 횟수를 저장한다.

# 2를 만들기 위해서 
# 1을 2배로 만들거나 or 1을 더한다

for i in range(1, target+1):
    dp[i] = min(dp[i-1]+1, i%2==0 and dp[int(i/2)]+1 or target, i%3==0 and dp[int(i/3)]+1 or target, dp[i])

print(dp[target]-1)