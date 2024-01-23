import sys
input = sys.stdin.readline

# n:나무 수, m:나무 길이
n, m = map(int,input().split())
heights = list(map(int,input().split()))

left, right = 1, max(heights)-1

# print(left,right)

# left가 right을 넘어서기 전까지
while left <= right:
    mid = (left + right) // 2

    cut_length = 0
    for height in heights:
        if not height - mid<0:
            cut_length += height - mid

    # print(left,right,mid,cut_length, m)

    # 자른 길이가 길면, left 올리기
    if cut_length >= m:
        left = mid+1
    # 자른 길이가 짧으면, right 내리기
    else:
        right = mid-1

print(right)