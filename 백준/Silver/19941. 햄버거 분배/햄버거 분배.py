import sys
import math
from collections import deque
input = sys.stdin.readline


N, K = map(int,input().split())

lst = list(input().strip())
cnt = 0
for i in range(N):
    if lst[i] == 'H':
        for j in range(2*K+1):
            check_idx = i-K+j
            if 0 <= check_idx < N:
                if lst[check_idx] == 'P':
                    lst[check_idx] = 'X'
                    lst[i] = 'X'
                    cnt += 1
                    break

print(cnt)