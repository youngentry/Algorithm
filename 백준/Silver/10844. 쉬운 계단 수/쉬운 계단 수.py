import sys
input = sys.stdin.readline

n = int(input())

if n==1:
  print(9)
else:
  dp = [[0]*10 for _ in range(n+1)]
  for i in range(1, 10):
    dp[1][i] = 1
  numbers = [0,1,2,3,4,5,6,7,8,9]

  for i in range(2,n+1):
    for number in numbers:
      if number == 0:
        dp[i][number] += dp[i-1][number+1] 
      elif number == 9:
        dp[i][number] += dp[i-1][number-1] 
      else:
        dp[i][number] += dp[i-1][number-1] + dp[i-1][number+1] 

  print(sum(dp[-1])%1000000000)