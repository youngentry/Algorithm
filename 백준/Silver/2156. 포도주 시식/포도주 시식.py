import sys

input = sys.stdin.readline

# n:정수 개수, s:target
n = int(input())
numbers =[0] + [int(input()) for _ in range(n)]

dp = [0]*(n+1)

if n == 1:
    print(numbers[1])
elif n == 2:
    print(numbers[1]+numbers[2])
else:
    dp[1] = numbers[1]
    dp[2] = numbers[1] + numbers[2]
    dp[3] = max(numbers[1]+numbers[3], numbers[2]+numbers[3], numbers[1]+numbers[2])


    for i in range(4,n+1):
        dp[i] =max(dp[i-3]+numbers[i]+numbers[i-1], dp[i-2] + numbers[i], dp[i-1] ) 

    print(max(dp))