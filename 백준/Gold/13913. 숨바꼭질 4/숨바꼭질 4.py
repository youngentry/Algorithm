import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int,input().split())

arr = [100000]*200001
v = [0]*200001
if N==K:
    print(0)
    print(N)
elif K<N:
    print(-(K-N))
    for i in range(N,K-1,-1):
        print(i,end=' ')
else:
    # x,move,route
    q = deque([[N,0,[N]]])
    mn = 100000
    ans = None

    while q:
        x,move,route = q.popleft()


        if move >= mn:
            continue

        if x == K and mn > move:
            mn = min(mn,move)
            ans = route
            continue

        # move가 작다면 이동
        nx = move+1
        if x+1 <= 200000 and arr[x+1] > nx and v[x+1] == 0:
            v[x+1] = 1
            arr[x+1] = nx
            q.append([x+1,nx,route+[x+1]])
        if 0<= x-1 and arr[x-1] > nx and v[x-1] == 0:
            v[x-1] = 1
            arr[x-1] = nx
            q.append([x-1,nx,route+[x-1]])
        if x*2 <= 200000 and arr[x*2] > nx and v[x*2] == 0:
            v[x*1] = 1
            arr[x*2] = nx
            q.append([x*2,nx,route+[x*2]])

    print(mn)
    for num in ans:
        print(num,end=' ')
