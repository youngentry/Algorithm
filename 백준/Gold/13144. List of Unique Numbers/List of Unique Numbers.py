import sys
input = sys.stdin.readline

# start_time = time.time()
# ======================================

# 수열의 길이 N, 삭제 횟수 K
N = int(input())
nums = list(map(int,input().split()))

l,r = 0,0
cnt = 1
seq = set()
seq.add(nums[0])

while True:
    if r+1 < N:
        # 넣으려는 수가 들어 있으면 왼쪽 줄이기
        if nums[r+1] in seq:
            seq.remove(nums[l])
            l += 1
        # 없으면 오른쪽 늘리고, set에 추가, 값 더하기
        else:
            r += 1
            seq.add(nums[r])
            cnt += len(seq)
    if r==N-1:
        break
print(cnt)

# ======================================
# print(time.time() - start_time)
