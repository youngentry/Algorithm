import sys
input = sys.stdin.readline

# ===================================================

def dfs(time, pos, size):
    global ans

    if pos == N-1:
        ans = max(ans,size)
        return

    # 시간 되면 종료
    if time == M:
        ans = max(ans,size)
        return

    if pos+1 < N:
        dfs(time+1, pos+1, size+arr[pos+1])
    if pos+2 < N:
        dfs(time+1, pos+2, (size//2)+arr[pos+2])


N, M = map(int,input().split())
arr = list(map(int,input().split()))

ans = 1
dfs(0,-1, 1)

print(ans)

# ===================================================
