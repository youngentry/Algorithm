
# C×R격자형
# 각 좌석의 번호는 해당 격자의 좌표 (x,y)
# 기다리고 있는 사람들은 제일 앞에서부터 1, 2, 3, 4, . 순으로 대기번호표를 받았다.
# 7*6
r,c = map(int,input().split())
k = int(input())

seats = [[0 for _ in range(c)] for _ in range(r)]
count = 0

x=0
y=0
dir = "R"

if c*r < k:
    print(0)
else:
    for i in range(c*r):
        seats[x][y]=i+1
        if i+1==k:
            print(x+1,y+1)
            break
        if dir == 'U' and (x == 0 or seats[x-1][y] != 0):
            dir = "R"
        elif dir == 'R' and (y == c - 1 or seats[x][y+1] != 0):
            dir = "D"
        elif dir == 'D' and (x == r - 1 or seats[x+1][y] != 0):
            dir = "L"
        elif dir == 'L' and (y == 0 or seats[x][y-1] != 0):
            dir = "U"

        if dir == 'U':
            x -= 1
        elif dir == 'R':
            y += 1
        elif dir == 'D':
            x += 1
        elif dir == 'L':
            y -= 1

