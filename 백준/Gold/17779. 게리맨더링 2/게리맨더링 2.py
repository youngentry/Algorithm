import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
diff = 987654321

def draw_line(arr,x,y,d1,d2):
    arr[x][y] = 1

    for i in range(d1+1):
        arr[x+i][y-i] = 5
        for j in range(x+i):
            for k in range(y-i+1):
                arr[j][k] = 1
                
    for i in range(d2+1):
        arr[x+i][y+i] = 5
        for j in range(x+i+1):
            for k in range(y+i+1,n):
                arr[j][k] = 2

    for i in range(d1+1):
        arr[x+d2+i][y+d2-i] = 5
        for j in range(x+d2+i+1,n):
            for k in range(y+d2-i,n):
                arr[j][k] = 4

    for i in range(d2+1):
        arr[x+d1+i][y-d1+i] = 5
        for j in range(x+d1+i,n):
            for k in range(y-d1+i):
                arr[j][k] = 3

    count = [0,0,0,0,0,0]
    for i in range(n):
        for j in range(n):
            count[arr[i][j]] += grid[i][j]

    global diff
    count[-1] += count.pop(0)
    diff = min(diff,max(count)-min(count))

for d1 in range(1,n):
    for d2 in range(1,n):
        for y in range(n):
            for x in range(n):
                tmp = [[0]*n for _ in range(n)]
                if 0<=y<y+d1+d2<n and 0<=x-d1<x<x+d2<n:
                    draw_line(tmp,y,x,d1,d2)

print(diff)