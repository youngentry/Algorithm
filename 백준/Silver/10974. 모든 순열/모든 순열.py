import sys
input = sys.stdin.readline

N = int(input())

path = []
v = [0]*(N+1)
def dfs(n):
    if n == N:
        print(' '.join(list(map(str,path))))
        return

    for i in range(1,N+1):
        if not v[i]:
            v[i] = 1
            path.append(i)
            dfs(n+1)
            v[i] = 0
            path.pop()

dfs(0)