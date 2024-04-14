import sys
input = sys.stdin.readline

def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y,parents):
    x = find_set(x)
    y = find_set(y)

    if x<y:
        parents[y] = x
    else:
        parents[x] = y

N,M = map(int,input().split())
parents = [i for i in range(N)]
for i in range(M):
    s,e = map(int,input().split())
    if i%2 == 1:
        if find_set(s) == find_set(e):
            print(i+1)
            break
        union(s,e,parents)
    else:
        if find_set(s) == find_set(e):
            print(i+1)
            break
        union(s,e,parents)
else:
    print(0)