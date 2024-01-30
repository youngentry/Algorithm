# 카운트정렬 풀이
for tc in range(10):
    dump_count = int(input())
    boxes = list(map(int,input().split()))

    while dump_count:
        counts = [0]*101 # 숫자 카운트 
        sorted_arr = [0]*100 # 숫자 정렬

        # 박스 숫자 카운트
        for box_num in boxes:
            counts[box_num] += 1

        # 누적합
        for i in range(1,101):
            counts[i] = counts[i-1] + counts[i]
        
        # 카운트 정렬    
        for i in range(99,-1,-1):
            counts[boxes[i]] -= 1
            sorted_arr[counts[boxes[i]]] = boxes[i]       
        
        left, right = 0, 99
        dump_count -= 1
        sorted_arr[left] +=1
        sorted_arr[right] -= 1
        
        # 재정렬을 위해 초기화
        boxes=sorted_arr

    print(f'#{tc+1} {max(boxes) - min(boxes)}')