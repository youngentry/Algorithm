import sys
input = sys.stdin.readline

def dfs(n,cur_node):
    for next_node in adj[cur_node]:
        if v[n][next_node]:
            continue

        v[n][next_node] = 1
        dfs(n, next_node)


N = int(input())
graph = [list(map(int,input().split())) for _ in  range(N)]

v = [[0]*N for _ in range(N)]
adj = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j]:
            adj[i].append(j)

for i in range(N):
    dfs(i,i)

for i in range(N):
    print(" ".join(map(str,v[i])))
