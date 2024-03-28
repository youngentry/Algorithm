import sys
input = sys.stdin.readline

# st = time.time()
# ======================================

def vim(v,x,y,dir_arr):
    v[x][y] = "#"
    for dx,dy in dir_arr:
        nx,ny = x+dx,y+dy
        while v[nx][ny] != 6:
            v[nx][ny] = "#"
            nx,ny = nx+dx,ny+dy

def dfs(n,start):
    global ans
    if n==cctv_cnt:
        v = [grid[i][:] for i in range(N+2)]
        for k in range(cctv_cnt):
            x,y,cnum = cctvs[k]
            vim(v,x,y,dirs[cnum][path[k]])

        cnt = 0
        for p in range(N+2):
            for q in range(M+2):
                if v[p][q] == 0:
                    cnt += 1
        # print(cnt)
        ans = min(ans,cnt)
        # print(*v,sep='\n')
        return

    for i in range(4):
        path.append(i)
        dfs(n+1, i)
        path.pop()


N,M = map(int,input().split())
wall = [6] * (M+2)
grid = [wall]
cctvs = []
dirs = [
    [],
    [[(0,1)],[(1,0)],[(0,-1)],[(-1,0)]],
    [[(0,1),(0,-1)],[(1,0),(-1,0)],[(0,1),(0,-1)],[(1,0),(-1,0)]],
    [[(-1,0),(0,1)],[(0,1),(1,0)],[(0,-1),(1,0)],[(-1,0),(0,-1)]],
    [[(-1,0),(0,1),(0,-1)],[(-1,0),(0,1),(1,0)],[(0,1),(1,0),(0,-1)],[(-1,0),(0,-1),(1,0)]],
    [[(0,1),(0,-1),(1,0),(-1,0)],[(0,1),(0,-1),(1,0),(-1,0)],[(0,1),(0,-1),(1,0),(-1,0)],[(0,1),(0,-1),(1,0),(-1,0)]],
]
for i in range(N):
    line = list(map(int,input().split()))
    for j in range(M):
        if 1 <= line[j] <= 5:
            cctvs.append((i+1,j+1,line[j]))
    grid.append([6]+line+[6])
grid.append(wall)
# print(*grid,sep='\n')
# print(cctvs)

arr = [0,1,2,3,4]
cctv_cnt = len(cctvs)
check = [0] * cctv_cnt
path = []
ans = int(2e9)
dfs(0,0)

print(ans)

# ======================================
# print(time.time() - st)
