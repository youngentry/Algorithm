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

    # 홀수번 톱니끼리, 짝수번 톱니끼리 같은 방향 회전
    for i in range(1,5):
        if i%2 == number%2:
            is_change[i-1][1] = dir
        else:
            is_change[i-1][1] = -dir

    # [톱니번호, 회전방향]에 따라 회전
    for i in range(4):
        if is_change[i][0]:
            turn(i,is_change[i][1])

def turn(number,dir):
    if dir == 1: # 시계
        topnis[number].insert(0,topnis[number].pop())
    elif dir == -1: # 반시계
        topnis[number].append(topnis[number].pop(0))

# 회전 명령에 따라 수행
for number, dir in spins:
    rotate(number,dir)

# 12시 톱니에 따라 결과 반환
count = 0
for i in range(4):
    if topnis[i][0] == 1:
        count+=2**i

print(count)