import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
from collections import deque
import heapq
import time
from math import floor

# st = time.time()
# ======================================

def in_order(node,row):
    global col

    if node <= N and node != -1:
        in_order(graph[node][0],row+1)
        # print(node,row,col)
        v[row].append((node,col))
        col += 1
        in_order(graph[node][1],row+1)



has_parent = set()
N = int(input())
graph = [ [-1,-1] for _ in range(N+1)]
for i in range(1,N+1):
    node,l,r = map(int,input().split())
    if l != -1:
        graph[node][0] = l
        has_parent.add(l)
    if r != -1:
        graph[node][1] = r
        has_parent.add(r)

all_nodes = set([i for i in range(1,N+1)])
# 1~N 만큼의 배열을 만듬
v = [[] for _ in range(N+1)]
root = list(all_nodes - has_parent).pop()
# print("root:",root)
col = 1
in_order(root,0)
# print(v)
ans = [0,0]
for i in range(len(v)):
    if len(v[i])>1:
        tmp_width = v[i][-1][1] - v[i][0][1] +1
        if tmp_width > ans[1]:
            ans = [i+1,tmp_width]
    else:
        if ans == [0,0]:
            ans = [1,1]


print(" ".join(map(str,ans)))

# ======================================
# print(time.time() - st)
