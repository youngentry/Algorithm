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

times = []
for i in range(N):
    times.append(list(map(int,input().split())))

times.sort(key=lambda x:(x[0],x[1]))

rooms = []
heappush(rooms, times[0][1])

for i in range(1, len(times)):
    # 새로운 강의가 현재 진행중인 강의가 끝나는 시간보다 늦게 시작하면
    if times[i][0] >= rooms[0]:
        heappop(rooms) # 현재 강의를 제거
    heappush(rooms, times[i][1]) # 그렇지 않다면 새 강의실 추가

print(len(rooms))

# ======================================
# print(time.time() - st)
