import sys
from collections import deque

input = sys.stdin.readline

m,n = map(int, input().split())

box = []

# 벽 만들기
wall = ["0"]*(m+2)
box.append(wall)
for _ in range(n):
  row = list(map(int, input().split()))
  box.append(["0"] +row + ["0"])
box.append(wall)
# print(box)

def bfs(starts):
  queue = deque(starts)
  max_count = 0
  # print(queue)
  while len(queue):
    x,y,count = queue.popleft()
    max_count = count
    # print(x,y,count,"?")
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
      nx,ny = x+dx, y+dy
      # print(nx,ny,"123", box[nx][ny])
      if box[nx][ny] == 0:
        box[nx][ny] = 1
        queue.append((nx,ny,count+1))
  else:
    return max_count

def findStarts():
  starts = []
  for i in range(len(box)):
    for j in range(len(box[0])):
      if box[i][j]==1:
        starts.append((i,j,0))

  return starts

starts = findStarts()

# print(starts)

result = bfs(starts)

# print(box)

def checkBox():
  isRipen = True
  for i in range(len(box)):
    for j in range(len(box[0])):
      if box[i][j] == 0:
        isRipen = False
        i = len(box)
        break
  if not isRipen:
    return -1

if checkBox() == -1:
  print(-1)
else:
  print(result)
