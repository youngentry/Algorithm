import copy

N,M,V = map(int, input().split())
routes = {}

# 노드 초기화
routes = {i: [] for i in range(1, N+1)}

# 그래프 생성
for info in range(M):
    node, route =map(int,input().split())

    # 간선 추가
    routes[node].append(route)
    routes[route].append(node)

# 간선 정렬
for key in routes.keys():
    routes[key] = sorted(routes[key])

dfs_routes = copy.deepcopy(routes)
bfs_routes = copy.deepcopy(routes)

dfs_result =[]
dfs_visited = [False for _ in range(N+1)]

def dfs(start):
    dfs_visited[start] = True
    dfs_result.append(start)
    for next_node in routes[start]:
        if not dfs_visited[next_node]:
            dfs(next_node)

dfs(V)

bfs_visited = [False for _ in range(N+1)]
bfs_visited[V] = True 
bfs_result =[]
queue = [V]

while len(queue):
    start_node = queue.pop(0)
    bfs_result.append(start_node)

    for next_node in routes[start_node]:
        if not bfs_visited[next_node]:
            queue.append(next_node)
            bfs_visited[next_node] = True

print(*dfs_result)
print(*bfs_result)