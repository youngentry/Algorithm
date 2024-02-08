# 색종이의 장수 N 1~100
# 평면은 가로 1001, 세로 1001

# 왼쪽아래 a,b 너비 c,d

n = int(input())

grid = [[0 for _ in range(1001)] for _ in range(1001)]

for t_c in range(n):
    a,b,c,d = map(int,input().split())
    for i in range(a,a+c):
        for j in range(b,b+d):
            grid[i][j] = t_c+1

filtered_grid = [[number for number in row if number != 0] for row in grid]

answer = []
for t_c in range(n):
    count = 0
    for row in filtered_grid:
        for number in row:
            if number == t_c+1:
                count +=1
    answer.append(count)


for width in answer:
    print(width) 