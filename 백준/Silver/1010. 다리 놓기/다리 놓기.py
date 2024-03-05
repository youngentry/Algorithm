import sys

N = int(input())
numbers = [list(map(int,input().split())) for _ in range(N)]

# 조합 경우의 수는 다음과 같이 구한다.
# n! / r! * (n-r)!
for n,m in numbers:
    ans = 1

    for i in range(1,m+1):
        ans *= i
    for i in range(1,n+1):
        ans //= i
    for i in range(1,m-n+1):
        ans //= i
        
    print(ans)