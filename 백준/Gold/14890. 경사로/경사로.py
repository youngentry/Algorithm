import sys
input = sys.stdin.readline

n,l = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

def check(arr):
    idx = 0
    able_length = 1
    while idx < n-1:
        # 높이가 같으면 앞으로 이동, 판을 놓을 수 있는 거리 증가
        if arr[idx] == arr[idx+1]:
            idx += 1
            able_length += 1
            continue
        
        # 높이가 2이상 차이나면 종료
        if abs(arr[idx]-arr[idx+1]) >= 2:
            return False
        
        # 높은 곳으로 이동하는 경우
        # 높이차가 1이면, 판을 놓을 수 있는지 확인
        if arr[idx]-arr[idx+1] == -1 and able_length >= l:
            idx += 1 # 전진
            able_length = 1 # 거리 초기화
            continue

        # 낮은 곳으로 이동하는 경우
        if arr[idx]-arr[idx+1] == 1:
            # 아래로 판을 놓을 수 있는지 확인
            if idx+l>=n:
                return False
            for j in range(1,l+1):
                if arr[idx]-arr[idx+j] != 1:
                    return False                    

            idx += l
            able_length = 0 # 거리 초기화
            continue

        return False
        
    return True


count = 0
for i in range(n):
    if check(grid[i]):
        count += 1
    tmp_arr = []
    for j in range(n):
        tmp_arr.append(grid[j][i])
    if check(tmp_arr):
        count += 1

print(count)