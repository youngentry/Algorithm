import sys
input = sys.stdin.readline

# st = time.time()
# ======================================

# 놓인 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
N,d,k,c = map(int,input().split())

nums = []
for i in range(N):
    nums.append(int(input()))
nums = nums+nums
l = 0

c_dict = {}
c_dict[c] = 1
for num in nums[l:l+k]:
    if c_dict.get(num):
        c_dict[num] += 1
    else:
        c_dict[num] = 1

mx = len(c_dict)
# 초밥 순회 매드무비
while l < N:
    to_remove = nums[l]
    l += 1
    next = nums[l+k-1]

    # left 초밥 제거
    if c_dict.get(to_remove) == 1:
        del c_dict[to_remove]
    else:
        c_dict[to_remove] -= 1

    # right 초밥 추가
    if c_dict.get(next):
        c_dict[next] += 1
    else:
        c_dict[next] = 1

    mx = max(mx,len(c_dict))

print(mx)

# ======================================
# print(time.time() - st)
