import sys
input = sys.stdin.readline

# 3의 배수 판정 => 각 자리수의 합이 3의 배수
N = list(sorted(input().strip()))
sm = 0
for i in range(len(N)):
    sm += int(N[i])

if sm%3 == 0 and N.count("0"):
    print("".join(list(sorted(N,reverse=True))))
else:
    print(-1)

