import sys
input = sys.stdin.readline

# st = time.time()
# ======================================

# 놓인 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
N,K = map(int,input().split())
nums = list(map(int,input().split()))

l,r = 0,0

long_dict = {}
for i in range(1,100_001):
    long_dict[i] = 0
long_dict[nums[0]] += 1
cnt = 1
mx = 1
while True:
    if l == N-1 and r == N-1:
        break

    # 오른쪽 늘릴 수 있으면
    if r+1 < N and long_dict[nums[r+1]] + 1 <= K:
        r += 1
        long_dict[nums[r]] += 1
        cnt += 1
    # 아니면 왼쪽 줄이기
    else:
        long_dict[nums[l]] -= 1
        cnt -= 1
        l += 1

    mx = max(mx, cnt)

print(mx)

# ======================================
# print(time.time() - st)
