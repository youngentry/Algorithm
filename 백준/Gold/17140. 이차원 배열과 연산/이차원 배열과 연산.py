import sys
input = sys.stdin.readline

def count_sort(arr):
    max_num = max(arr)
    # 한 행 또는 열에 있는 수를 정렬하려면, 각각의 수가 몇 번 나왔는지 알아야 한다.
    count_arr = [[i,0] for i in range(max_num+1)]
    for num in arr:
        count_arr[num][1] += 1
    count_arr.pop(0)
    count_arr.sort(key=lambda x: (x[1],x[0]))
    new_row = []
    for num,count in count_arr:
        if count != 0:
            new_row.append(num)
            new_row.append(count)

    return new_row[:100]
    

r,c,k = map(int,input().split()) 
grid = [list(map(int,input().split())) for _ in range(3)]
time = 0
max_row_size = len(grid) 
max_col_size = len(grid[0]) 
#  k가 되기 위한 최소 시간 or 100초가 지나도 A[r][c] = k가 되지 않으면
flag = True
if len(grid)>r-1 and len(grid)>c-1 and grid[r-1][c-1] == k:
    print(0)
else:
    while time < 100:
        # # R연산: 행의 개수 ≥ 열의 개수
        new_arr = []
        if max_row_size >= max_col_size:
            cur_col_size = 0

            # print("R연산",time)

            for i in range(len(grid)):
                sorted_arr = count_sort(grid[i])
                sorted_arr_size = len(sorted_arr)
                new_arr.append(sorted_arr)
                if cur_col_size < sorted_arr_size:
                    cur_col_size = sorted_arr_size
            # R 연산이 적용된 경우에는 가장 큰 행을 기준으로 모든 행의 크기가 변하고
            for row in new_arr:
                size_diff = cur_col_size - len(row)
                for _ in range(size_diff):
                    row.append(0)
            
            # 찾았다면 종료
            if len(new_arr) > r-1 and len(new_arr[0]) >c-1 and new_arr[r-1][c-1] == k:
                # print(*new_arr,sep='\n')
                time += 1
                break
            # 새로운 배열로 변환
            grid = new_arr
            # 사이즈 갱신
            max_col_size = cur_col_size     
        

        # # C연산: 행의 개수 < 열의 개수
        elif max_row_size < max_col_size:
            # print("C연산",time)
            cur_col_size = 0

            # col로 이루어진 배열 만들기
            col_grids = []
            for j in range(len(grid[0])):
                tmp = []
                for i in range(len(grid)):
                    tmp.append(grid[i][j])
                col_grids.append(tmp)

            # 정렬 수행
            for i in range(len(col_grids)):
                sorted_arr = count_sort(col_grids[i])
                sorted_arr_size = len(sorted_arr)
                new_arr.append(sorted_arr)
                if cur_col_size < sorted_arr_size:
                    cur_col_size = sorted_arr_size

            # C 연산이 적용된 경우에는 가장 큰 열을 기준으로 모든 열의 크기가 변하고
            for row in new_arr:
                size_diff = cur_col_size - len(row)
                for _ in range(size_diff):
                    row.append(0)
            
            # 전치행렬로 뒤집기
            reversed_grid = [list(row) for row in zip(*new_arr)]

            # 찾았다면 종료
            if len(reversed_grid) > r-1 and len(reversed_grid[0]) >c-1 and reversed_grid[r-1][c-1] == k:
                # print(*reversed_grid,sep='\n')
                time += 1
                break
            # 새로운 배열로 변환
            grid = reversed_grid
            
            max_row_size = cur_col_size     

        time += 1

    else:
        flag = False
        print(-1)

    if flag:
        print(time)
