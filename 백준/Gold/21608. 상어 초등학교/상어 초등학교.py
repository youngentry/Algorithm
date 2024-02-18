import sys
input = sys.stdin.readline

n = int(input())
wall = [[0] * (n+2)]
grid =wall + [[0]+[-1]*(n)+[0] for _ in range(n)] + wall
infos = [list(map(int,input().split())) for _ in range(n*n)]

# 교실의 가장 왼쪽 윗 칸은 (1, 1)
# 가장 오른쪽 아랫 칸은 (N, N)

# 한 칸에는 학생 한 명의 자리만 있을 수 있고, 
# |r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸이 
# (r1, c1)과 (r2, c2)를 인접하다고 한다

# 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.

# 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.

# 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 

directions = [[-1,0],[0,1],[1,0],[0,-1]] 
# 학생 수 만큼 반복
for num,*loves in infos:
    # print(*grid,sep='\n')
    # print('------------')
    result1 = []
    # 1번 진행
    # => 빈칸을 찾는다. 
    # => 4방탐색으로 좋아하는 학생을 카운트 한다. 
    # => 좋아하는 학생이 가장 많은 좌표를 저장한다.
    # => 좋아하는 학생이 가장 많은 좌표가 한개이면 그 좌표로 앉힌다. => 종료한다.
    for i in range(1,n+1):
        for j in range(1,n+1):
            if grid[i][j] == -1:
                love_count = 0
                for di,dj in directions:
                    ni,nj = i+di,j+dj
                    if grid[ni][nj] in loves:
                        love_count += 1
                result1.append((i,j,love_count))
    # 한 명이면 앉히고 종료
    if len(result1) == 1:
        x,y,count = result1[0]
        grid[x][y] = num
        continue
    
    # 한 명이 아니면 정렬하고 가장 높은 숫자 앉히고 종료
    result1.sort(key=lambda x:x[2], reverse=True)
    if result1[0][2] != result1[1][2]:
        x,y,count = result1[0]
        grid[x][y] = num
        continue
    max_1_count = result1[0][2]
    tmp_1_count = 0
    for x,y,count in result1:
        if count != max_1_count:
            tmp_1_count += 1
    for _ in range(tmp_1_count):
        result1.pop()
    
    # 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
    # => 복수의 좋아하는 학생이 가장 많은 좌표에 대해 인접한 칸을 카운트한다.
    # => 비어있는 칸이 가장 많은 칸이 한개이면 그 좌표로 앉힌다. => 종료한다.
    result2 = []
    for i,j,_ in result1:
        space_count = 0
        for di,dj in directions:
            ni,nj = i+di, j+dj
            if grid[ni][nj] == -1:
                space_count += 1
        result2.append((i,j,space_count))

    # 한 명이면 앉히고 종료
    if len(result2) == 1:
        x,y,count = result2[0]
        grid[x][y] = num
        continue
    # 한 명이 아니면 정렬하고 가장 높은 숫자 앉히고 종료
    result2.sort(key=lambda x:x[2], reverse=True)

    if result2[0][2] != result2[1][2]:
        x,y,count = result2[0]
        grid[x][y] = num
        continue
    max_2_count = result2[0][2]
    tmp_2_count = 0
    for x,y,count in result2:
        if count != max_2_count:
            tmp_2_count += 1
    for _ in range(tmp_2_count):
        result2.pop()
    # 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 
    #    그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
    # => 2에서 구한 복수의 비어있는 칸이 가장 많은 좌표들에 대해 
    # => 행-열 순으로 정렬을 한다.
    # => 해당 칸에 앉힌다.
    max_space = result2[0][2]
    result3 = []
    for x,y,count in result2:
        if count == max_space:
            result3.append((x,y))
    result3.sort(key=lambda x:(x[0],x[1]))
    # print(result3)
    # print("?????????????????????/")
    grid[result3[0][0]][result3[0][1]] = num

# print(*grid,sep='\n')
dict = {}
for info in infos:
    num,*loves = info
    dict[num] = loves
final_sum = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        count = 0
        loves = dict[grid[i][j]]
        for di,dj in directions:
            ni,nj = i+di,j+dj
            if grid[ni][nj] in loves:
                count += 1
        # print(count)
        # print(10**(count))
        final_sum += 10**(count)//10

print(final_sum)