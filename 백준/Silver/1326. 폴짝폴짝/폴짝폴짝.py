import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
numbers =[0] + list(map(int,input().split()))
a,b = map(int,input().split())

min_num = 10001

queue = deque([[a,1]])
visited = [0] * (10000+1)

while queue:
    idx, count = queue.popleft()
    for i in range(idx, n+1, numbers[idx]):
        if i == b:
            min_num = min(min_num,count)
        if visited[i] == 0:
            visited[i] = count
            queue.append([i,count+1])
    for i in range(idx, 0, -numbers[idx]):
        if i == b:
            min_num = min(min_num,count)
        if visited[i] == 0:
            visited[i] = count
            queue.append([i,count+1])
if visited[b]:
    print(visited[b])
else:
    print(-1)