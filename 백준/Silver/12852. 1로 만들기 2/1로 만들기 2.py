import sys
input = sys.stdin.readline

mx = sys.maxsize
N = int(input())
init_int = N
size = int(1e6)+1
arr = [mx]*(size)
arr[1] = 0

for i in range(1,size+1):
    if i*3 < size:
        arr[i*3] = min(arr[i]+1, arr[i*3])
    if i*2 < size:
        arr[i*2] = min(arr[i]+1, arr[i*2])
    if i+1 < size:
        arr[i+1] = min(arr[i]+1, arr[i+1])

remain = arr[N]
ans = [N]
while remain > 0:
    if N%3==0 and arr[N//3] == remain - 1:
        ans.append(N//3)
        N //= 3
    elif N%2==0 and arr[N//2] == remain - 1:
        ans.append(N//2)
        N //= 2
    elif arr[N]-1 == remain - 1:
        ans.append(N-1)
        N -= 1
    remain-=1
print(arr[init_int])
print(" ".join(map(str,ans)))