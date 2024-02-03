import sys
input = sys.stdin.readline

n,m = map(int,input().split())
numbers = list(map(int,input().split()))

left, right = 0,0

cur_sum = 0
count =0
while left<n:
    # left:0, right:0 인덱스에서 시작
    # cur_sum이 m보다 작다면, 현재 인덱스 숫자를 더하고, right 다음으로
    if right!=n and cur_sum < m :
        cur_sum += numbers[right]
        right+=1
    else:
    # 그 외에는 cur_sum이 m보다 커진 경우이니 현재 인덱스 숫자를 빼고 left 다음으로
        cur_sum -= numbers[left]
        left+=1

    if cur_sum == m:
        count+=1

print(count)