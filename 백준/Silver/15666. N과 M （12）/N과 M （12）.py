import sys
input = sys.stdin.readline


def dfs(n,start):
    global N
    global M
    global num_set

    if n==M:
        print(" ".join(map(str,path)))
        return

    for i in range(start,len(nums)):
        path.append(nums[i])
        dfs(n+1,i)
        path.pop()

N,M = map(int,input().split())
nums = sorted(set(list(map(int,input().split()))))
num_set = set()
path = []
dfs(0,0)
rst = sorted(list(num_set))
