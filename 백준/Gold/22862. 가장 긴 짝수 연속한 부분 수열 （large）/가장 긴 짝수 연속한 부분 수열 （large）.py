import sys
input = sys.stdin.readline

# start_time = time.time()
# ======================================

# 수열의 길이 N, 삭제 횟수 K
N,K = map(int,input().split())
nums = list(map(int,input().split()))

l, r = 0, 0
length = 0
mx = 0
# 짝수로 시작
if nums[0] % 2 == 0:
    length += 1
    mx += 1
else:
    K -= 1

while True:

    # 다음 오른쪽 수가
    if r+1 < N:
        # 짝수번이면 그냥 늘리기
        if nums[r+1] % 2 == 0:
            r += 1
            length += 1
        else:
            # 홀수번을 만나면
            # 삭제 할 수 있다면 오른쪽을 늘림
            if K >= 1:
                K -= 1
                r += 1
            else:
                # 삭제할 수 없다면 왼쪽을 당기는데,
                # 홀수면 K++
                if nums[l] % 2 == 1:
                    K += 1
                    l += 1
                # 짝수면 length--
                else:
                    l += 1
                    length -= 1
    mx = max(mx, length)

    if r == N-1:
        break

print(mx)

# ======================================
# print(time.time() - start_time)
