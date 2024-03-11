import sys
input = sys.stdin.readline

word = input().strip()
N = len(word)

divisors = []
for i in range(1,N+1):
    if N%i == 0:
        divisors.append(i)
R,C = 0,0
size = len(divisors)
if size%2==1:
    R = C = divisors[size//2]
else:
    R = divisors[size//2-1]
    C = divisors[size//2]

arr = [[None]*C for _ in range(R)]

cnt = 0
r = c = 0
while cnt < N:
    arr[r][c] = word[cnt]
    cnt += 1
    
    r+=1
    if r%R == 0:
        r=0
        c+=1

ans = ""

for i in range(R):
    for j in range(C):
        ans += arr[i][j]

print(ans)