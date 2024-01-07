from collections import deque

n, m = map(int, input().split())

# 미로 생성
maze = [['0' for _ in range(m + 2)]]
for _ in range(n):
  maze.append(list('0' + input().strip() + '0'))
maze.append(['0' for _ in range(m + 2)])

# 미로 탐색
queue = deque([[1, 1, 0]])
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
move = 0
maze[1][1] = "0"

while len(queue):
  x, y, move = queue.popleft()

  if x == n and y == m:
    print(move+1)
    break

  # 상하좌우 방문
  for dx, dy in direction:
    nx, ny = x + dx, y + dy
    if maze[nx][ny] == '1':
      queue.append([nx,ny, move+1])
      maze[nx][ny] = '0'