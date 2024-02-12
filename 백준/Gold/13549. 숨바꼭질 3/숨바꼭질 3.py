import sys
import heapq
input = sys.stdin.readline

n,k = map(int,input().split())

# print(n,k)
size = 100_000+1
inf = float('inf')
visited = [inf]*(size)
visited[n] = 0
# print(visited)

queue = []
heapq.heappush(queue,[0,n])
move_count = 0

directions = [[-1,1],[1,1],[0,0]]
while queue:
    move,x = heapq.heappop(queue) 

    # k에 도달 시 종료
    if x==k:
        move_count = move
        break   

    for dx, plus in directions:
        if plus == 0:
            nx = x*2
        else:
            nx = x+dx

        if 0<=nx<size:
            n_move = move+abs(plus)
            if n_move < visited[nx]:
                visited[nx] = n_move
                heapq.heappush(queue,[n_move,nx])

# print(visited)
print(move_count)