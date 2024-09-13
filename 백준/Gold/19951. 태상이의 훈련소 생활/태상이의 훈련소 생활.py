import heapq
import sys
from _collections import deque
from copy import deepcopy
from heapq import heappush

N,M = map(int,input().split())
heights = [0] + list(map(int,input().split())) + [0]
orders = []
# for _ in range(M):
#     orders.append(list(map(int,input().split())))
# orders.sort()
# print(orders)
#
# acc = 0
# orders = deque(orders)
# hq = []
#
# for i in range(1,100_001):
#     while orders and orders[0] == i:
#         sidx,fidx,val = orders.popleft()
#         acc += order[sval]
#         heappush(hq,(fidx,val))
#     # while 시작이 같으면 acc ++ 하고 heap에 (종료,acc) 추가
#     # while 종료가 같으면 acc -- 하고 heap에서 제거
#
#     heights[i] += acc # 최종 높이를 적용
#     pass

arr = [0]*(N+1) + [0]

for i in range(M):
    a,b,k = map(int,input().split())
    arr[a] += k
    arr[b+1] -= k


idx = 0
acc = 0
while idx <= N:
    idx += 1
    acc += arr[idx]

    heights[idx] += acc
print(' '.join(map(str,heights[1:-1])))
