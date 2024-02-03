import sys

input = sys.stdin.readline

n,m = map(int,input().split())
numbers = list(map(int,input().split()))

left, right = 0,0

cur_sum = 0
count =0
while left<n:
    # print("cur:",cur_sum,count,"L:",left,"R:",right,)
    if right!=n and cur_sum < m :
        cur_sum += numbers[right]
        right+=1
    else:
        cur_sum -= numbers[left]
        left+=1
    if cur_sum == m:
        count+=1

print(count)