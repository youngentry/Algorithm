import sys
from collections import deque

input = sys.stdin.readline

# bfs로 연결된 단지 확인,
# 단지 크기 저장
# 순회하며 만나는 단지에 순서 입력

n = int(input())

# 맵 만들기
grids = []
wall = ["0" for _ in range(n+2)]
grids.append(wall)
for _ in range(n):
  user_input = list(input().rstrip())
  grid = ["0"] + user_input + ["0"]
  grids.append(grid)
grids.append(wall)

# queue = deque([[1,1,0]])
# buildings = []

# while len(queue):
#   x,y,count = queue.popleft()
#   print(x,y,count)

#   for i in range(1,n+1):
#     for j in range(1,n+1):
#       if grids[i][j] == "0":
#         buildings.append(count)
#         count = 0
#       for direction in directions:
#         dx, dy = direction
#         nx, ny = x + dx, y + dy
#         if grids[nx][ny] == '1':
#           grids[nx][ny] = '0'
#           queue.append([nx,ny,count+1])

# print(grids)

directions = [[-1,0],[1,0],[0,-1],[0,1]]



def bfs(sx,sy):
  count = 0
  queue = deque([[sx,sy]])
  grids[sx][sy] = '0'
  while len(queue):
    x, y = queue.popleft()
    count +=1
    for direction in directions:
      dx, dy = direction
      nx, ny = x + dx, y + dy
      if grids[nx][ny] == '1':
        grids[nx][ny] = '0'
        queue.append([nx,ny])
  else:
    if count != 0:
      return count
  
counts = []

for i in range(1,n+1):
  for j in range(1,n+1):
    if grids[i][j] == "1":
      count = bfs(i,j)
      counts.append(count)

print(len(counts))
for count in sorted(counts):
  print(count)
