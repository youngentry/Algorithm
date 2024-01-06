# 호텔 정문으로부터 걸어서 가장 짧은 거리에 있는 방을 선호
# W 개의 방이 있는 H 층 건물 (1~99)
# 엘리베이터는 가장 왼쪽

T = int(input())

for T_C in range(1,T+1):
    H, W, N = map(int,input().split())
    
    hotel = [[0 for _ in range(W)] for _ in range(H)]


    for i in range(H):
        for j in range(W):
            hotel[i][j] += (i+1)*100 + j+1
    
    # print(hotel)
    count = 0

    for i in range(W):
        for j in range(H):
            count+=1

            if (count==N):
                print(hotel[j][i])