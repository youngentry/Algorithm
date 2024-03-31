import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
from collections import deque
from heapq import heappush, heappop
import time
from math import floor

# st = time.time()
# ======================================

N = int(input())

lines = [tuple(map(int,input().split())) for _ in range(N)]
lines.sort()

left,right = lines[0]
ans = right - left

for i in range(1, N):
    next_left, next_right = lines[i]

    # 다음 오른쪽이 범위 이내면 볼 것 없음
    if right >= next_right:
        continue
    # 다음 왼쪽이 오른쪽에 붙어있고 오른쪽이 넓으면, 넓어진 만큼 더함
    elif next_left <= right and right < next_right:
        ans += next_right - right
        right = next_right
    # 다음 왼쪽이 오른쪽과 떨어져 있으면
    elif next_left > right:
        left = next_left
        right = next_right
        ans += right-left
print(ans)


# ======================================
# print(time.time() - st)
