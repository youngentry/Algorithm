import sys

t = int(input())
for tc in range(t):
    p = input().strip()
    n = int(input())
    numbers = input().strip()[1:-1].split(",")

    # left, right 좌표를 (0,n)으로 설정
    # "D"연산 시 
    # if reverse=False => left+1 
    # if reverse=True => right+1
    left, right = 0, n
    is_bad = False
    is_flipped = False
    for alpha in p:
        if alpha == "R":
            is_flipped = not is_flipped
        if alpha == "D":
            if left==right:
                is_bad = True
                break
            if is_flipped:
                right -= 1
            else:
                left += 1
    if is_bad:
        print('error')
    else:
        # reverse=True라면 배열 뒤집어서 출력
        if is_flipped:
            print(str(list(map(int,numbers[left:right][::-1]))).replace(" ",""))
        else:
            print(str(list(map(int,numbers[left:right]))).replace(" ",""))

