import sys
input = sys.stdin.readline

N,M = map(int,input().split())
numbers =sorted(list(map(int,input().split())))
used = [0]*N
path = []
def dfs(size):
    if len(path) == size:
        for num in path:
            print(num,end=' ')
        print()
        return


    for i in range(N):
        path.append(numbers[i])
        dfs(size)
        path.pop()

dfs(M)
