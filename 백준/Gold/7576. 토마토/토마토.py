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
  box.append(["0"] + row + ["0"])
box.append(wall)

# BFS
def bfs(starts):
  queue = deque(starts)
  max_count = 0
  while len(queue):
    x,y,count = queue.popleft()
    max_count = count
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
      nx,ny = x+dx, y+dy
      if box[nx][ny] == 0:
        box[nx][ny] = 1
        queue.append((nx,ny,count+1))
  else:
    return max_count

# 시작지점 탐색
def findStarts():
  starts = []
  for i in range(len(box)):
    for j in range(len(box[0])):
      if box[i][j]==1:
        starts.append((i,j,0))
  return starts

# 익지 않은 도마도 확인
def checkUnripenTomatos():
  isRipen = True
  for i in range(len(box)):
    for j in range(len(box[0])):
      if box[i][j] == 0:
        isRipen = False
        i = len(box)
        break
  if not isRipen:
    return -1

starts = findStarts() # 시작 지점 찾기
result = bfs(starts) # queue에 시작지점 넣고 bfs
print(-1) if checkUnripenTomatos() == -1 else print(result) # 결과 출력