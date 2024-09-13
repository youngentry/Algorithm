import sys
input = sys.stdin.readline

N,M = map(int,input().split())
heights = [0] + list(map(int,input().split())) + [0]
orders = []
arr = [0]*(N+1) + [0]

for i in range(M):
    a,b,k = map(int,input().split())
    arr[a] += k
    arr[b+1] -= k


idx = 0
acc = 0
while idx <= N:
    idx += 1
    acc += arr[idx]
    heights[idx] += acc
    
print(' '.join(map(str,heights[1:-1])))