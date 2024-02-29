import sys
input = sys.stdin.readline 

def dfs(start):
    global N
    global M
    
    if len(path) == M:
        for i in range(M):
            print(path[i],end=" ")
        print()
        return
    
    for i in range(start,N):
        path.append(numbers[i])
        dfs(i)
        path.pop()

N,M = map(int,input().split())
numbers = sorted(list(map(int,input().split())))
path = []
dfs(0)