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
c_set = set(nums[l:l+k])
c_set.add(c)

mx = len(c_set)
# 초밥 순회 매드무비
while l < N:
    l += 1
    c_set = set(nums[l:l+k])
    c_set.add(c)
    mx = max(mx,len(c_set))

print(mx)

# ======================================
# print(time.time() - st)
