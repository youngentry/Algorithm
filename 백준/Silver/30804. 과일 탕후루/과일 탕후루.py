import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int,input().split()))

abstracted = [[numbers[0],1]]
idx = 0
for i in range(1,n):
    # 숫자가 같으면
    if abstracted[idx][0] == numbers[i]:
        abstracted[idx][1] += 1
    # 숫자가 다르면
    else:
        abstracted.append([numbers[i],1])
        idx+=1

# print(abstracted)

if len(abstracted)>1:
    max_num = abstracted[0][1] + abstracted[1][1]
    one = abstracted[0][0]
    two = abstracted[1][0]
    cur_num = abstracted[0][1]

    for i in range(1,len(abstracted)):
        left, right = abstracted[i-1], abstracted[i] 

        if (left[0]==one or left[0]==two) and (right[0]==one or right[0]==two): 
            cur_num += right[1]
            max_num = max(max_num,cur_num)
        else:
            cur_num = left[1] + right[1]
            max_num = max(max_num,cur_num)
        one, two = left[0], right[0]
    # 연속되는 숫자를 압축함
    # 붙어 있는 압축된 숫자들의 합이 가장 큰 경우를 반환
    print(max_num)
else:
    print(abstracted[0][1])