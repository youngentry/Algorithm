import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
diff = 987654321

def draw_line(x,y,d1,d2):
    arr = [[0]*n for _ in range(n)]
    arr[x][y] = 1

    # 1번 선거구
    for i in range(d1+1):
        arr[x+i][y-i] = 5
        for j in range(x+i):
            for k in range(y-i+1):
                arr[j][k] = 1
                
    # 2번 선거구
    for i in range(d2+1):
        arr[x+i][y+i] = 5
        for j in range(x+i+1):
            for k in range(y+i+1,n):
                arr[j][k] = 2

    # 4번 선거구
    for i in range(d1+1):
        arr[x+d2+i][y+d2-i] = 5
        for j in range(x+d2+i+1,n):
            for k in range(y+d2-i,n):
                arr[j][k] = 4

    # 3번 선거구
    for i in range(d2+1):
        arr[x+d1+i][y-d1+i] = 5
        for j in range(x+d1+i,n):
            for k in range(y-d1+i):
                arr[j][k] = 3

    # 선거구 긋기가 완료되었다면, 0,1,2,3,4,5 각각의 인구를 모두 합하기
    count = [0,0,0,0,0,0]
    for i in range(n):
        for j in range(n):
            count[arr[i][j]] += grid[i][j]

    count[-1] += count.pop(0) # 0,5번 인구 합치기 (5번 내에 0번이 존재) 

    # 가장 작인 인구 차이 구하기
    global diff
    diff = min(diff,max(count)-min(count))

for d1 in range(1,n):
    for d2 in range(1,n):
        for y in range(n):
            for x in range(n):
                if 0<=y<y+d1+d2<n and 0<=x-d1<x<x+d2<n:
                    draw_line(y,x,d1,d2)

print(diff)