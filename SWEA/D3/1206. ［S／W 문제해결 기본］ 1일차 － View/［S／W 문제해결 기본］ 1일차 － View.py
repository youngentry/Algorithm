for test_case in range(1,10 + 1):
    count = int(input())
    height = list(map(int,input().split()))

    # 좌우 두 칸 이내에
    # 더 높은 수가 없으면 카운트
    height_sum = 0
    for i in range(2, count-2):
        if height[i] > height[i-1] and height[i] > height[i-2] and height[i] > height[i+1] and height[i] > height[i+2]:
            height_sum += height[i] - max(height[i-1], height[i-2], height[i+1], height[i+2])

    print(f'#{test_case} {height_sum}')