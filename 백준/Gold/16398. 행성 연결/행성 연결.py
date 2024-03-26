import sys
from heapq import heappop, heappush
from collections import deque
# ==================================================

def u_find(x):
    if parents[x] == x:
        return x

    parents[x] = u_find(parents[x])
    return parents[x]


def u_union(x,y):
    x = parents[x]
    y = parents[y]

    if x==y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
parents = [i for i in range(N+1)]

list = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            list.append((graph[i][j],i,j))
list.sort()

cnt = 0
w_acc = 0
for w,s,e in list:
    # 부모가 같으면 싸이클이 발생하므로 넘기기
    if u_find(s) == u_find(e):
        continue

    # 집합끼리 union
    u_union(s,e)
    w_acc += w
    cnt += 1

    if cnt == N:
        break

print(w_acc)