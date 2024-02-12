import sys
from collections import deque
input = sys.stdin.readline

def transform(arr):
    print(arr,"?")
    return [int(arr[0]),arr[1]]

n = int(input())
k = int(input())
apples = [list(map(int,input().split())) for _ in range(k)]
l = int(input())
queue = deque([list(input().split()) for _ in range(l)])

# board 초기 세팅
board =[[9]*(n+2)] + [[9]+[0]*(n)+[9] for _ in range(n)] + [[9]*(n+2)]
board[1][1] = 1
for x,y in apples:
    board[x][y] = 5
# print(*board,sep='\n')

dict = {'L':-1,'D':1}

dirs = [[-1,0],[0,1],[1,0],[0,-1]]
toward = 1
time = 0
body = deque([[1,1]])
while True:
    # print(queue,"queue")



    # 향하는 방향+1 칸이 자기몸 '1'이나 벽 '9'이면 종료
    # print(body,'body')
    head = body[-1]
    # print(head,"head")
    dx,dy = dirs[toward%4]
    nx,ny = head[0]+dx, head[1]+dy
    if board[nx][ny] == 9 or board[nx][ny] == 1:
        break
    # print(nx,ny, time)
    # print(*board,sep='\n')

    # 머리 다음칸에 위치
    body.append([nx,ny])
    time += 1

        # 방향 전환
    if queue and int(queue[0][0]) == time:
        sec, direction = queue.popleft()
        toward += dict[direction]

    # 사과면 머리 추가하고 다음으로
    if board[nx][ny] == 5:
        board[nx][ny] = 1
        continue

    board[nx][ny] = 1
    # 일반 땅이면 꼬리 하나 제거하고 다음으로
    del_x, del_y = body.popleft()
    board[del_x][del_y] = 0

print(time+1)    

# print(*board,sep='\n')