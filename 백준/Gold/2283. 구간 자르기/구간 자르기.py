import sys
input = sys.stdin.readline

# start_time = time.time()
# ======================================

# N개 선분, K 목표
N,K = map(int,input().split())
lines = [tuple(map(int,input().split())) for _ in range(N)]
lines.sort()
memo = [0]*1_000_001

# 시작 숫자가 같을 때마다 cnt++, memo에 더해줌
cnt = 0
where = 0
idx = 0
while where < 1_000_001:
    while idx < len(lines) and lines[idx][0] == where:
        cnt += 1
        if idx < len(lines):
            idx += 1
    else:
        memo[where] += cnt
        if where == 1_000_001:
            break
        where += 1
# 시작 숫자가 같을 때마다 cnt--, memo에 더해줌
lines.sort(key=lambda x:x[1])
cnt = 0
where = 0
idx = 0
while where < 1_000_001:
    while idx < len(lines) and lines[idx][1] == where:
        cnt += 1
        if  idx < len(lines):
            idx += 1
    else:
        memo[where] -= cnt
        if where == 1_000_001:
            break
        where += 1

l,r = 0,0
acc = memo[0]
ans = (0,0)
while l < 1_000_000 and r < 1_000_000:
    if acc == K:
        ans = (l,r+1)
        break
    elif acc < K:
        r += 1
        acc += memo[r]
    else:
        acc -= memo[l]
        l += 1
print(" ".join(map(str,ans)))

# ======================================
# print(time.time() - start_time)
