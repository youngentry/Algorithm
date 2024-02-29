import sys
input = sys.stdin.readline 

N,M,start_node = map(int,input().split())

grid = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    go, to = map(int,input().split())
    grid[go].append(to)
    grid[to].append(go)

stack = [start_node]
count = 0
while stack:
    node = stack.pop()
    if visited[node] == 0:
        count += 1
        visited[node] = count
    for next_node in sorted(grid[node],reverse=True):
        if visited[next_node] == 0:
            stack.append(next_node)

for i in range(1,N+1):
    print(visited[i])
