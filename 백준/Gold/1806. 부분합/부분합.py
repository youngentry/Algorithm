import sys
input = sys.stdin.readline

N, S= map(int,input().split())
numbers = list(map(int,input().split()))
last_idx = N-1

# 합이 더 크면 left +1
# 최소 길이보다 더 길면 left +1
left = 0
right = 0
cur_sum = numbers[0]
min_length = sys.maxsize

if cur_sum == S:
    print(1)
else:
    while True:
        if cur_sum < S and right+1 <= last_idx:
            right+=1
            cur_sum += numbers[right]
        elif cur_sum >= S or left+1 <= last_idx:
            cur_sum -= numbers[left]
            left+=1
        if cur_sum >= S:                               # 그 합이 S 이상이 되는 것 중
            min_length = min(min_length, right-left+1) # 가장 짧은 길이 갱신
        if left == last_idx and right == last_idx:
            break

    if min_length == sys.maxsize:
        print(0)
    else:
        print(min_length)