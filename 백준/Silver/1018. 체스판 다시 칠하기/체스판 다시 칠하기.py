import sys

input = sys.stdin.readline

n,m = map(int,input().split())

grid = []
for i in range(n):
    grid.append(list(input().strip()))

def check(i,j):
    tmp_grid1 = grid[:]
    tmp_count1 = 0
    tmp_grid2 = grid[:]
    tmp_count2 = 0

    # W 스타트
    for x in range(i,i+8):
        for y in range(j,j+8):
            if (x+y)%2 == 0 and tmp_grid1[x][y]=="B" :
                tmp_count1 +=1
            elif (x+y)%2 == 1 and tmp_grid1[x][y]=="W":
                tmp_count1 +=1
                
    # B 스타트
    for x in range(i,i+8):
        for y in range(j,j+8):
            if (x+y)%2 == 0 and tmp_grid2[x][y]=="W" :
                tmp_count2 +=1
            elif (x+y)%2 == 1 and tmp_grid2[x][y]=="B":
                tmp_count2 +=1
                
    return min(tmp_count1,tmp_count2)

results = []

for i in range(n-7):
    for j in range(m-7):
        results.append(check(i,j))

print(min(results))