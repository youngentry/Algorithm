import sys
sys.setrecursionlimit(100000)
from collections import deque
import heapq
import time
input = sys.stdin.readline
from math import floor

# st = time.time()
# ======================================

N = int(input())
table = []
dp = [0] * (N+1)
for i in range(N):
    day,revenue = map(int,input().split())
    table.append((day,revenue))

for i in range(N-1,-1,-1):
    day, revenue = table[i]
    dp[i] = max(dp[i], dp[i+1])
    if i+day <= N:
        dp[i] = max(dp[i+1], revenue+dp[i+day])

print(max(dp))

# ======================================
# print(time.time() - st)
