import sys
input = sys.stdin.readline

N = input().strip() # str.strip()으로 "\n" 과 같은 탈출 문자 제거
lst = list(map(int, input().split())) 

check_list = [lst[0]]

count = -1
for num in lst:
    # 첫번째 방법, in으로 확인하기
    # num이 check에 없으면 넣고, 있으면 count +1
    if num not in check_list:
        check_list.append(num)
    else:
        count+=1

    # 두번째 방법, for문으로 in을 구현하기
    # is_visited = False
    # for j in range(len(check_list)):
    #     # num이 check_list 중 하나라도 같다면 is_visited를 True로 변경
    #     if num == check_list[j]:
    #         is_visited = True
    #         break
    # # is_visited가 True라면 이미 방문객이 있다는 것이므로 count +1
    # if is_visited:
    #     count+=1
    # else:
    #     # is_visited가 False라면 check_list에 추가
    #     check_list.append(num)

# print(check_list)
print(count)

