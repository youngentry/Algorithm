import sys
input = sys.stdin.readline

N,M = map(int,input().split())
numbers =sorted(list(map(int,input().split())))
used = [0]*N
path = []
size = M
def dfs(start):
    global N
    global size

    # 사이즈에 도달하면 종료
    if len(path) == size:
        for i in path:
            print(i,end=" ")
        print()
        return

    for i in range(start,N):
        if used[i] == 0:
            used[i] = 1
            path.append(numbers[i])
            dfs(i+1)
            path.pop()
            used[i] = 0

dfs(0)