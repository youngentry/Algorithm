import sys
input = sys.stdin.readline

n = int(input())

star = [["*"]*n for _ in range(n)]

def punch(start, size):
    x,y = start
    if size < 3:
        return
    for i in range(x+size//3,x+size//3*2):
        for j in range(y+size//3,y+size//3*2):
                star[i][j] = " "
    
    for i in range(3):
        for j in range(3):
            punch([x+size//3*i, y+size//3*j], size//3) 

punch([0,0], n)

for i in range(n):
    print("".join(star[i]))