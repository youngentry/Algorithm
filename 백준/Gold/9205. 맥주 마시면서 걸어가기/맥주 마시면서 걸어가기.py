import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
line = 32768
def transform(str):
    return int(str) + line

for tc in range(t):
    n = int(input())
    home = list(map(transform,input().split()))
    cons = [home]
    for _ in range(n):
        cons.append(list(map(transform,input().split())))
    fes = list(map(transform,input().split())) 
    cons.append(fes)
    # print(cons)

    visited = [0]*(n+2)
    # print(visited)

    queue = deque([home])
    visited[0] = 1

    is_happy = False
    while queue:
        cx,cy = queue.popleft()
        # print(queue,visited)
        for i in range(1,n+2):
            nx,ny = cons[i]
            # print(nx,ny)
            # print(abs(nx-cx),abs(ny-cy))
            if abs(nx-cx)+abs(ny-cy)<=1000 and visited[i] == 0:
                if nx==fes[0] and ny==fes[1]:
                    is_happy = True
                    queue.clear()
                    break
                else:
                    visited[i] = 1
                    queue.append(cons[i])

    if is_happy:
        print("happy")
    else:
        print('sad')



    # 조건에 들어오는 편의점이 있나? (n만큼 for문 돌림)
        # 락페 지점인가?
            # 종료
        # 락페 지점이 아니다
            # 방문처리, queue에 넣음