from itertools import permutations

N,M,K = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]

dirs = ((-1,0),(0,1),(1,0),(0,-1))
def dfs(sx,sy,d,cur_count,finish_count):
    if cur_count == finish_count:
        return
    nx,ny = sx+dirs[d][0],sy+dirs[d][1]
    temp_grid[sx][sy],temp_grid[nx][ny] = temp_grid[nx][ny],temp_grid[sx][sy]
    dfs(nx,ny,d,cur_count+1,finish_count)


def turn(x,y,size):
    dfs(x-size,y-size,2,0,size*2)
    dfs(x+size,y-size,1,0,size*2)
    dfs(x+size,y+size,0,0,size*2)
    dfs(x-size,y+size,3,0,size*2-1)


turns = []
for _ in range(K):
    R,C,S = map(int,input().split())
    R-=1
    C-=1
    turns.append([R,C,S])

permus = list(permutations(turns,K))
result = 987654321
# M번의 회전 연산 수행
for permu in permus:
    temp_grid = [grid[row][:] for row in range(N)]
    for R,C,S in permu:
        for i in range(1,S+1):
            turn(R,C,i)

    for trow in temp_grid:
        result = min(result, sum(trow))

print(result)