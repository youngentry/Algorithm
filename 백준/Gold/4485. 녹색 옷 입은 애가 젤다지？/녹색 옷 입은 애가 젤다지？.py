import sys
import heapq

input = sys.stdin.readline
inf = 987654321

flag = True
tc = 1
while flag:
    n = int(input())
    if n == 0:
        flag = False
        break

    grid = []
    for i in range(n):
        grid.append(list(map(int,input().split())))

    queue = []
    heapq.heappush(queue,[grid[0][0],0,0])
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    visited = [[inf]*n for _ in range(n)]
    visited[0][0] = 0
    while queue:
        # print('--------------')
        # print(*grid,sep='\n')
        # print('-')
        # print(*visited,sep='\n')
        # print(queue)
        cur_lose,x,y = heapq.heappop(queue)
        # print(cur_lose,x,y)

        if x==n-1 and y==n-1:
            print(f'Problem {tc}:',cur_lose)
            tc+=1
            break

        for dx,dy in directions:
            nx,ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n:
                new_lose = cur_lose + grid[nx][ny]
                if new_lose < visited[nx][ny]:
                    visited[nx][ny] = new_lose
                    heapq.heappush(queue,[new_lose,nx,ny])
