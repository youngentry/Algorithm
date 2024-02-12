import sys
from itertools import permutations
input = sys.stdin.readline

# 입력 받기
n = int(input())
numbers = list(map(int,input().split()))
# 덧셈,뺄셈,곱셈,나눗셈
oper_input = list(map(int,input().split()))
operators = list('+'*oper_input[0] + '-'*oper_input[1]+ '*'*oper_input[2]+'/'*oper_input[3])
oper_permus = list(permutations(operators,n-1))

max_num = int(-2e9)
min_num = int(2e9)
for permu in oper_permus:
    cur_num = numbers[0]
    for i in range(n-1):
        if permu[i] == "+":
            cur_num += numbers[i+1]
        elif permu[i] == "-":
            cur_num -= numbers[i+1]
        elif permu[i] == "*":
            cur_num *= numbers[i+1]
        elif permu[i] == "/":
            if cur_num>0:
                cur_num = cur_num // numbers[i+1]
            elif cur_num<0:
                # 음수인 경우 양수로 바꾼 뒤 몫을 취하고 그 몫을 음수로
                cur_num = -((-cur_num) // numbers[i+1]) 

    max_num = max(max_num, cur_num)
    min_num = min(min_num, cur_num)

print(max_num,min_num)