import sys
input = sys.stdin.readline

def dfs(n):
    global cnt

    if n == N:
        if len(path) <= 1:
            return
        if max(*path) - min(*path) >= X:
            if L <= sum(path) <= R:
                cnt += 1
        return

    path.append(difs[n])
    dfs(n+1)
    path.pop()
    dfs(n+1)


N, L, R, X = map(int,input().split())
difs = list(map(int,input().split()))

cnt = 0
path = []
dfs(0)
print(cnt)
