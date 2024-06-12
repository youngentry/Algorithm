N = int(input())
grid = [0]*366

for i in range(N):
    s,e = map(int,input().split())
    for j in range(s,e+1):
        grid[j] += 1

total = 0
idx = 0
while idx < 365:
    idx += 1

    w,h = 0,0
    while idx < 366 and grid[idx]:
        h = max(h,grid[idx])
        w += 1
        idx += 1
    total += w*h

print(total)