import sys
from collections import deque
input = sys.stdin.readline

# 입력 받기
N,K = map(int,input().split())
numbers = list(map(int,input().split()))

def rotate():
    down_q.append(up_q.pop())
    up_q.appendleft(down_q.popleft())

# 로봇은 컨베이어 위를 이동함
# 로봇을 올리는 위치에 올리거나, 로봇이 어떤 칸으로 이동하면 해당 칸 내구도 즉시 1감소
# 1번칸이면 올림, N번칸이면 내림

# 1. 벨트가 로봇과 함께 회전함
# 2. 가장 먼저 올라간 로봇부터 벨트 회전방향으로 1칸 이동할 수 있으면 이동, 이동할 수 없으면 가만히
# 1. 로봇이 이동하려면 이동하려는 칸에 로봇이 없고, 내구도 1이상 있어야 함
# 3. 올리는 위치의 칸이 내구도 0이 아니면 로봇을 올림
# 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정 종료, 아니면 1번으로 돌아감

# 길이가 2N인 벨트가 N인 컨베이어 위아래를 감싸며 돌고 있음
up_q = deque([[i,False] for i in numbers[:N]])
down_q = deque([[i,False] for i in numbers[N:][::-1]])

count = 0
attempt = 0
# 내구도가 0인 칸의 개수가 K이상이면 종료
while count < K:
    attempt += 1
    # 1. 벨트가 로봇과 함께 회전함
    rotate()
    
    # 로봇을 내릴 위치라면 내림
    if up_q[-1][1] == True:
        up_q[-1][1] = False
    
    for i in range(N-2,-1,-1):
        dur,is_dom = up_q[i]
        # 현재 로봇이 있고, 다음칸 로봇이 없고, 다음 칸의 내구도가 있으면 전진
        if is_dom and up_q[i+1][1] == False and up_q[i+1][0]:
            up_q[i][1] = False
            up_q[i+1][1] = True
            up_q[i+1][0] -= 1

            # 내구도 카운트
            if up_q[i+1][0] == 0:
                count += 1

    # 로봇을 내릴 위치라면 내림
    if up_q[-1][1] == True:
        up_q[-1][1] = False

    # 올리는 위치의 칸에 내구도가 있으면 로봇 올림
    if up_q[0][0]:
        up_q[0][1] = True
        up_q[0][0] -= 1
        if up_q[0][0] == 0:
            count += 1

print(attempt)