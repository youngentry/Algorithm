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
# 1. 왼쪽에 하나를 넣고 시작
left_mn_h = [-1*int(input())]
right_mx_h = []
print(left_mn_h[0]*-1)
# print(left_mn_h, right_mx_h)
for i in range(1,N):
    num = int(input())

#     print(num,'num')
    if len(left_mn_h) == len(right_mx_h):
    # 3. 길이가 같고, 삽입하려는 값이 기준보다 크면,  오른쪽에 삽입, 왼쪽으로 이동
    # 2. 길이가 같고, 삽입하려는 값이 기준보다 작으면, 왼쪽에 삽입
        if -1*left_mn_h[0] <= num:
            heappush(right_mx_h,num)
            popped = heappop(right_mx_h)
            heappush(left_mn_h,-1*popped)
        else:
            heappush(left_mn_h,-1*num)

    # 4. 왼쪽의 길이가 길고, 삽입하려는 값이 기준보다 크면, 오른쪽에 삽입
    # 5. 왼쪽의 길이가 길고, 삽입하려는 값이 기준보다 작으면, 왼쪽에 삽입 + 왼쪽을 오른쪽으로 이동
    elif len(left_mn_h) > len(right_mx_h):
        if -1*left_mn_h[0] <= num:
            heappush(right_mx_h,num)
        else:
            heappush(left_mn_h,-1*num)
            popped = heappop(left_mn_h)
            heappush(right_mx_h,-1*popped)

    # 4. 오른쪽의 길이가 길고, 삽입하려는 값이 기준보다 크면, 오른쪽에 삽입 + 오른쪽을 왼쪽으로
    # 5. 오른쪽의 길이가 길고, 삽입하려는 값이 기준보다 작으면, 왼쪽에 삽입
    elif len(left_mn_h) < len(right_mx_h):
        if -1*left_mn_h[0] < num:
            heappush(right_mx_h,num)
            popped = heappop(right_mx_h)
            heappush(left_mn_h,-1*popped)
        else:
            heappush(left_mn_h,-1*num)

#     print(left_mn_h, right_mx_h)
    print(left_mn_h[0]*-1)

# ======================================
# print(time.time() - st)
