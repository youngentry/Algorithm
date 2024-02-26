import sys
input = sys.stdin.readline 

n,k = map(int,input().split())
numbers = [int(input().strip()) for _ in range(n)]
dp = [0]*(k+1)
dp[0] = 1

for number in numbers:
    for j in range(1,k+1):
        if j-number >= 0:
            dp[j] += dp[j-number]
# 아래의 식은 일차원 배열로 변경할 수 있음
# dp[i-1]항은 현재 항과 동일하므로 새로운 가능성을 +1 해주는 방식으로 처리 가능

# for i in range(1,n+1):
#     for j in range(1,k+1):
#         if j-numbers[i] >= 0:
#             # (새로운 동전을 이용해 새롭게 만들 수 있다면)
#             # 지금까지 만들어 온 횟수 + 새로운 동전을 사용해 만든 횟수(1개 추가)
#             dp[i][j] = dp[i-1][j]+dp[i][j-numbers[i]] 
#         else:
#             # (새로운 동전을 이용할 수 없다면) 
#             # 지금까지 만들어 온 횟수
#             dp[i][j] = dp[i-1][j] 

print(dp[k])