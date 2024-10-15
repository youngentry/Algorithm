import sys
from _collections import deque
from idlelib.pyparse import C_NONE

input = sys.stdin.readline

N,M = map(int,input().split())
max_num = int(2e9)

# a시작,b도착,c시간

edges = []
dis = [max_num] * (N+1)
for i in range(M):
    edges.append((tuple(map(int,input().split()))))

def bf(start):
    dis[start] = 0

    for i in range(N):
        for j in range(M):
            cnode,nnode,cost = edges[j]
            if dis[cnode] != max_num and dis[nnode] > dis[cnode] + cost:
                dis[nnode] = dis[cnode] + cost
                if i == N - 1:
                    return True
    return  False

is_negative_cycle = bf(1)

if is_negative_cycle:
    print(-1)
else:
    for i in dis[2:]:
        if i == max_num:
            print(-1)
        else:
            print(i)