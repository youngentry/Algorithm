import sys
input = sys.stdin.readline

N,M = map(int,input().split())
nums = sorted([int(input()) for _ in range(N)])

ans = 2000000000

left = 0
right = 1
if nums[1]-nums[0] >= M:
    ans = min(nums[1]-nums[0], ans)
while not (left==N-1 and right == N-1):
    diff = nums[right] - nums[left]
    if left == right:
        right += 1
        diff = nums[right] - nums[left]
    # M보다 작으면 right +1
    elif diff < M and right != N-1:
        if right < N-1:
            right += 1
        diff = nums[right] - nums[left]
    # 크거나 같으면 left +1
    else:
        if left < N-1:
            left += 1
        diff = nums[right] - nums[left]
        
    if diff<=ans and diff >= M:
        ans = nums[right] - nums[left]

print(ans)