import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int,input().split()))

arrow_map = {}
for i in range(0,1_000_002):
    arrow_map[i] = 0

arrow_count = 0
for i in range(N):
    if arrow_map[arr[i]] > 0:
        arrow_map[arr[i]] -= 1
        arrow_map[arr[i]-1] += 1
    else:
        arrow_map[arr[i]-1] += 1
        arrow_count += 1

print(arrow_count)

