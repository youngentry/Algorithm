import sys

input = sys.stdin.readline

n,m = map(int,input().split())

numbers = []
for i in range(n):
    for j in range(m):
        numbers.append(i+1)

combs = []
def get_comb(cur, idx, flag):
    if idx == m:
        # for i in range(1,m):
        #     if cur[i-1]>cur[i]:
        #         flag = False
        # if flag:
        print(*cur)
        return

    for i in range(idx,n*m,m):
        # print(cur, numbers[i])
        if len(cur)==0 or len(cur)>=1 and cur[-1]<=numbers[i]:
            cur.append(numbers[i])
            get_comb(cur[:],idx+1, True)
            cur.pop()

if m == 1:
    for i in range(n):
        print(i+1)
else:
    get_comb([],0, True)

# print(combs)