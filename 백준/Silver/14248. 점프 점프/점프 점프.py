import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
numbers =[0] + list(map(int,input().split()))
s = int(input())

queue = deque([s])
visited = [0] * (100000+1)
visited[s] = 1
while queue:
    idx = queue.popleft()
    left = idx-numbers[idx] >= 1 and idx-numbers[idx]
    right = idx+numbers[idx] < n+1 and idx+numbers[idx]
    if left>=1 and visited[left] == 0:
        visited[left] = 1
        queue.append(left)
    if right>=1 and visited[right] == 0:
        visited[right] = 1
        queue.append(right)

print(sum(visited))