import sys
sys.setrecursionlimit(25000)
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()
ans = 0
for i in range(N):
    # 예상등수A - 실제등수B
    ans += abs(numbers[i]-(i+1))
print(ans)