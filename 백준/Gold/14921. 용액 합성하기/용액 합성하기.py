import sys
input = sys.stdin.readline

# st = time.time()
# ======================================

N = int(input())
numbers = list(map(int,input().split()))
numbers.sort()

l,r = 0, N-1
dif = int(2e9)
ans = [numbers[0],numbers[N-1]]

while l < r:
    cur_sum = numbers[l] + numbers[r]
    # 0 찾으면 종료
    if cur_sum == 0:
        dif = 0
        ans = [numbers[l], numbers[r]]
        break

    if abs(cur_sum) < abs(dif):
        dif = cur_sum
        ans = [numbers[l], numbers[r]]
    # 합이 0보다 크면 오른쪽 당기기
    if cur_sum > 0:
        r -= 1
    # 합이 0보다 작으면 왼쪽 당기기
    elif cur_sum < 0:
        l += 1
print(dif)

# ======================================
# print(time.time() - st)
