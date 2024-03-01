N = int(input())
numbers = [0] + list(map(int,input().split()))
dp = [0]*(N+1)
dp2 = [0]*(N+1)

for i in range(1,N+1):
    max_count = 0
    for j in range(i):
        if numbers[j] < numbers[i]: # 작은 값을 이루는 수열 중 가장 긴 수열을 선택
            max_count = max(dp[j]+1, max_count)
    dp[i] = max_count

# 반대로도 수행
numbers2 = [0] + list(reversed(numbers))
for i in range(1,N+1):
    max_count = 0
    for j in range(i):
        if numbers2[j] < numbers2[i]:
            max_count = max(dp2[j]+1, max_count)
    dp2[i] = max_count
    
dp.pop(0)
dp2.reverse()
dp2.pop()

# n번째 idx에서 증가하는 수열, 감소하는 수열의 합 중 가장 큰 결과 찾기
result = 0
for i in range(len(dp)):
    result = max(result, dp[i]+dp2[i])

print(result-1)