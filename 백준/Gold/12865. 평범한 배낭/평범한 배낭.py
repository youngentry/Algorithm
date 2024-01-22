import sys

input = sys.stdin.readline

n,k = map(int,input().split())

dp = [[0]*(k+1) for _ in range(n+1)]

items = [[0,0]]
for i in range(n):
    w,v = map(int,input().split())
    items.append([w,v])

for i in range(1,k+1):
    capable = i
    for j in range(1,n+1):
        wei,val= items[j]
        
        # 현재 가방에 담긴 가치 갱신
        dp[j][i] = dp[j-1][i]

        # 현재 아이템을 넣을 무게가 되면 넣기
        if capable >= wei:
            # (현재 가방에 담긴 가치), (새로운 가치 + 남은 여분 무게 만큼 가치) 비교
            dp[j][i] = max(dp[j][i], val + dp[j-1][i-wei])
            
print(dp[-1][-1])