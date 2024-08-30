N,K = map(int,input().split())
nums = list(map(int,list(input())))

# print(N,K,nums)

stack = []
use_count = 0
for i in range(0, len(nums)):
    while stack and stack[-1] < nums[i] and use_count < K:
        stack.pop()
        use_count += 1
    stack.append(nums[i])

# print(use_count,stack)
while use_count < K:
    if stack:
        stack.pop()
    use_count += 1

# print(use_count,stack)
if stack:
    print(''.join(map(str,stack)))
else:
    print(0)