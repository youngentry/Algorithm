import sys
input = sys.stdin.readline

# K개의 랜선을 잘라서 모두 N개의 같은 길이의 랜선으로
# N개보다 많이 만드는 것도 N개를 만드는 것에 포함 ( N >= K 면 OK)
# 최대 랜선의 길이는?

# 이것도 이분탐색으로
# 가장 작은걸로 자른 몫이 11보다 큰지 확인

k,n = map(int,input().split())
lines = [ int(input()) for _ in range(k)]
sorted_lines = sorted(lines)

left = 1
right = sorted_lines[-1]

while left <= right:
    mid = (left + right) // 2

    # 자르는 크기 mid에 따른 랜선 수 체크 
    cut_count = 0
    for line in lines:
        cut_count += line // mid

    # 랜선의 수가 n보다 크거나 같으면 left 높이고
    if cut_count >= n:
        left = mid + 1
    # 랜선의 수가 n보다 작으면 right 낮추고
    else:
        right = mid - 1

print(right)