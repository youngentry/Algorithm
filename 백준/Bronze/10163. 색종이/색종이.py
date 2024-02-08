import sys
input = sys.stdin.readline

# 입력
n = int(input())
arr = [[0]*1001 for _ in range(1001)]
for k in range(1,n+1):
    x1,y1,x2,y2 = list(map(int,input().split()))
    for i in range(x1,x1+x2):
        for j in range(y1,y1+y2):
            arr[i][j] = k

cnts = [0]*(n+1)
for row in arr:
    for j in row:
        cnts[j] += 1

print(*cnts[1:],sep='\n')