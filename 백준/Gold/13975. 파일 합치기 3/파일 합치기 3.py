import sys
from collections import deque
from heapq import heappush,heappop
import time
input = sys.stdin.readline
# st = time.time()
# ======================================

T = int(input())
for tc in range(T):
    N = int(input())
    bytes = list(map(int,input().split()))

    pq = []
    for byte in bytes:
        heappush(pq,byte)

    acc = 0
    while len(pq) >= 2:
        a = heappop(pq)
        b = heappop(pq)
        tmp_sum = a+b
        acc += tmp_sum
        heappush(pq, tmp_sum)

    print(acc)
# ======================================
# print(time.time() - st)