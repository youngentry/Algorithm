import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    x,y = map(int,input().split())
    arr.append((x,y))

ans = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            x1,y1 = arr[i]
            x2,y2 = arr[j]
            x3,y3 = arr[k]

            a,b,c = (x2-x1)**2 + (y2-y1)**2 , (x3-x2)**2 + (y3-y2)**2, (x1-x3)**2 + (y1-y3)**2

            if a+b==c or b+c==a or c+a==b:
                ans += 1 

print(ans)