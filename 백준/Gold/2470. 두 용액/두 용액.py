def transform(str_int):
    num = int(str_int)
    if num>=0:
        return [abs(int(str_int)), 1]
    else:
        return [abs(int(str_int)), -1]

N = int(input())
base_numbers = list(map(int,input().split()))
numbers = sorted(map(transform,base_numbers))

min_num = 2e9
a,b = None,None
a_b = []
for i in range(N-1):
    # 부호가 다른 경우
    if numbers[i][1]*numbers[i+1][1] == -1:
        if min_num >= abs(numbers[i+1][0] - numbers[i][0]):
            min_num = abs(numbers[i+1][0] - numbers[i][0])
            a_b.append((numbers[i+1],numbers[i]))
    # 부호가 같은 경우
    else:
        if min_num >= abs(numbers[i+1][0] + numbers[i][0]):
            min_num = abs(numbers[i+1][0] + numbers[i][0])
            a_b.append((numbers[i+1],numbers[i]))

candidates = []
for tuple in a_b:
    x,y = tuple
    candidates.append([x[0]*x[1], y[0]*y[1]])

for candidate in candidates:
    candidate.sort()
    if abs(candidate[0]+candidate[1]) == min_num:
        print(candidate[0],candidate[1])