T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())

    grid = [[0 for _ in range(n)] for _ in range(n)]
    print(f'#{test_case}')

    count = 1
    x, y = [0, 0]
    direction = "R"

    for i in range(n*n):
        grid[x][y]=count
        count+=1
        if (direction=="U") and (x == 0 or grid[x-1][y] != 0):
            direction="R"
        if (direction=="R") and (y+1 == n or grid[x][y+1] != 0):
            direction="D"
        if (direction=="D") and (x+1 == n or grid[x+1][y] != 0 ):
            direction="L"
        if (direction=="L") and (y == 0 or grid[x][y-1] != 0):
            direction="U"

        if (direction=="R"):
            y+=1
        if (direction=="D"):
            x+=1
        if (direction=="L"):
            y-=1
        if (direction=="U"):
            x-=1

    for row in grid:
        print(" ".join(map(str,row)))