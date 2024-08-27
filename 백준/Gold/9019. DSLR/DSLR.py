from _collections import deque

# D: 더블 (10000으로 나눈 나머지)
def D(num):
    doubled_num = num * 2
    if doubled_num >= 10000:
        return doubled_num % 10000
    return doubled_num

# S: n-1 (0이라면 9999 저장)
def S(num):
    minused_num = num-1
    if minused_num == -1:
        return 9999
    return minused_num

# L: 왼쪽 회전
def L(num):
    stringified_num = list(str(num))
    while len(stringified_num) < 4:
        stringified_num = ['0'] + stringified_num
    stringified_num[0],stringified_num[1],stringified_num[2],stringified_num[3] = stringified_num[1],stringified_num[2],stringified_num[3],stringified_num[0]
    return int(''.join(stringified_num))

# R: 오른쪽 회전
def R(num):
    stringified_num = list(str(num))
    while len(stringified_num) < 4:
        stringified_num = ['0'] + stringified_num
    stringified_num[0],stringified_num[1],stringified_num[2],stringified_num[3] = stringified_num[3],stringified_num[0],stringified_num[1],stringified_num[2]
    return int(''.join(stringified_num))

N = int(input())
for i in range(N):
    num_set = set()
    origin_num, target_num = map(int,input().split())

    q = deque([(origin_num,'')])
    while q:
        cur_num, orders = q.popleft()
        if cur_num == target_num:
            print(orders)
            break

        D_num,S_num,L_num,R_num = D(cur_num), S(cur_num), L(cur_num), R(cur_num)

        if D_num not in num_set:
            num_set.add(D_num)
            q.append((D_num, orders + 'D'))
        if S_num not in num_set:
            num_set.add(S_num)
            q.append((S_num, orders + 'S'))
        if L_num not in num_set:
            num_set.add(L_num)
            q.append((L_num, orders + 'L'))
        if R_num not in num_set:
            num_set.add(R_num)
            q.append((R_num, orders + 'R'))


