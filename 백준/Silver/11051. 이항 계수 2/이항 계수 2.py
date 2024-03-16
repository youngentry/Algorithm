import sys
input = sys.stdin.readline

N,R = map(int,input().split())
# 5 4 3 2 1
# 2 1 3 2 1

# (N)!
# (R)! (N-R)!

ans = 1
for i in range(N-R+1,N+1):
    ans *= i

for j in range(1,R+1):
    ans //= j

print(ans%10007)