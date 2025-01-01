import sys
import math
from collections import deque
input = sys.stdin.readline


queue = deque(input().strip())

idx = 0
target = None

count = 1
while True:
    num = str(count)
    if not queue:
        break

    for i in range(len(num)):
        if queue and queue[0] == num[i]:
            target = num
            queue.popleft()

    count += 1


print(target)
