import sys

input = sys.stdin.readline

n, m = map(int,input().split())

results = []
def get_permutation(cur,i):
    if i==m:
        results.append(cur[:m])
        return
    
    for j in range(i ,n*m, m):
        cur[i], cur[j] = cur[j], cur[i] 
        get_permutation(cur,i+1)
        cur[i], cur[j] = cur[j], cur[i] 


numbers = [x for x in range(1, n+1) for _ in range(m)]
get_permutation(numbers, 0)


for result in results:
    print(*result)
    