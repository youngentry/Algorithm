import sys
input = sys.stdin.readline

topnis = [list(map(int,input().strip())) for _ in range(4)]

K = int(input())
spins = [list(map(int,input().split())) for _ in range(K)]

def rotate(number, dir):
    # 회전 여부 체크
    is_change = [[False,1],[False,1],[False,1]]
    # 톱니 사이 체크
    for i in range(3):
        if topnis[i][2] == 0 and topnis[i+1][6] == 1 or topnis[i][2] == 1 and topnis[i+1][6] == 0:
            is_change[i] = [True,1] 
    # 본래 톱니 추가
    is_change.insert(number-1, [True,1])

    # False 이후 톱니는 False로 변환 
    for i in range(number-2,-1,-1):
        if is_change[i+1][0]==False:
            is_change[i] = [False,1]
    for i in range(number,4):
        if is_change[i-1][0]==False:
            is_change[i] = [False,1]

    for i in range(1,5):
        # 1,3 번째고, 시계면
        if (number)%2 == 1 and dir == 1:
            # 1,3번째 1
            if i%2==1:
                is_change[i-1][1] = 1
            # 2,4번째 -1
            if i%2==0:
                is_change[i-1][1] = -1
        # 반시계면
        elif (number)%2 == 1 and dir == -1:
            if i%2==1:
                is_change[i-1][1] = -1
            # 2,4번째 -1
            if i%2==0:
                is_change[i-1][1] = 1
        # 2,4 번째고, 시계면
        elif (number)%2 == 0 and dir == 1:
            # 1,3번째 1
            if i%2==1:
                is_change[i-1][1] = -1
            # 2,4번째 1
            if i%2==0:
                is_change[i-1][1] = 1
        # 반시계면
        else:
            if i%2==1:
                is_change[i-1][1] = 1
            # 2,4번째 -1
            if i%2==0:
                is_change[i-1][1] = -1

    # [톱니번호, 회전방향]에 따라 회전
    for i in range(4):
        if is_change[i][0]:
            turn(i,is_change[i][1])


def turn(number,dir):
    if dir == 1: # 시계
        topnis[number].insert(0,topnis[number].pop())
    elif dir == -1: # 반시계
        topnis[number].append(topnis[number].pop(0))
    
# 회전 시키기 전 상태에서 맞닿은 톱니의 극이 같으면 무시
# 극이 다르면 회전 방향 반대로 회전을 시킨다
for number, dir in spins:
    rotate(number,dir)

count = 0
for i in range(4):
    if topnis[i][0] == 1:
        count+=2**i

print(count)