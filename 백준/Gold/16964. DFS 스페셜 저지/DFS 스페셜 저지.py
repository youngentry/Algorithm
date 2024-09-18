import math
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())


adj_arr = [set() for _ in range(100_001)]

for i in range(N-1):
    s,e = map(int,input().split())
    adj_arr[s].add(e)
    adj_arr[e].add(s)

check = list(map(int,input().split()))
line = '1 '
ord = 1

def dfs(x):
    global line
    global ord

    while adj_arr[x]:
        if ord >= N:
            return
        if check[ord] in adj_arr[x]:
            cur = check[ord]
            line += str(check[ord]) + ' '
            adj_arr[x].remove(check[ord])
            ord += 1
            dfs(cur)
        else:
            leaf_num = adj_arr[x].pop()
            if leaf_num == check[ord]:
                ord += 1
                line += str(leaf_num) + ' '

dfs(1)
# print(line)
if line.strip() == ' '.join(list(map(str,check))):
    print(1)
else:
    print(0)