import sys
input = sys.stdin.readline

def dfs(n):
    global N
    global M
    global num_set

    if n==M:
        if tuple(path) not in num_set:
            num_set.add(tuple(path))
        return

    for i in range(N):
        if v[i]==0:
            v[i] = 1
            path.append(nums[i])
            dfs(n+1)
            path.pop()
            v[i] = 0


N,M = map(int,input().split())
nums = sorted(list(map(int,input().split())))
num_set = set()
path = []
v = [0]*N
dfs(0)
for tup in sorted(list(num_set)):
    print(*tup)