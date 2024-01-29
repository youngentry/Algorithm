for tc in range(10):
    n = int(input())
    numbers = list(map(int,input().split()))

    memo = [0]*n

    for i in range(2,n-2):
        cur_hei = numbers[i]
        b1_hei = numbers[i-2]
        b2_hei = numbers[i-1]
        n1_hei = numbers[i+1]
        n2_hei = numbers[i+2]
        b_n_max_hei = max(b1_hei,b2_hei,n1_hei,n2_hei)

        # 현재 빌딩과 양쪽 빌딩 높이중 가장 높은 빌딩과의 차를 구함
        diff = cur_hei - b_n_max_hei

        # 차가 0보다 크면 memo에 기록
        if diff > 0:
            memo[i] += diff

    print(f'#{tc+1} {sum(memo)}')
