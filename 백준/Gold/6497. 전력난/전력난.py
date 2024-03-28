import sys
input = sys.stdin.readline

# st = time.time()
# ======================================

def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y):
    x = parents[x]
    y = parents[y]
    if x==y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

while True:
    N,M = map(int,input().split())
    if N==0 and M==0:
        break

    edges = []
    for _ in range(M):
        s,e,w = map(int,input().split())
        edges.append((w,s,e))

    edges.sort()
    parents = [i for i in range(N)]
    cnt = N
    acc = 0
    mx = 0
    for w,s,e in edges:
        mx += w
        if find_set(s) == find_set(e):
            continue

        union(s,e)
        acc += w
        cnt += 1

        if cnt == N:
            break

    print(mx-acc)

# ======================================
# print(time.time() - st)
