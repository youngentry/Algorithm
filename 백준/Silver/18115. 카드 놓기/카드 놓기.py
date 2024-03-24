import sys
sys.setrecursionlimit(100000)  # 재귀 깊이 제한 설정
from collections import deque
import heapq
import time
input = sys.stdin.readline  # 입력 속도를 높이기 위해 sys.stdin.readline 사용

# st = time.time()
# ======================================

N = int(input())
numbers = list(map(int,input().split()))
numbers.reverse()
cards = deque([i for i in range(1,N+1)])
arr = deque()
n = 1

for i in range(N):
    if numbers[i] == 1:
        arr.appendleft(n)
    elif numbers[i] == 2:
        arr.insert(1,n)
    elif numbers[i] == 3:
        arr.append(n)
    n += 1

print(" ".join(map(str,arr)))



# ======================================
# print(time.time() - st)
