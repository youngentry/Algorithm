import sys
input = sys.stdin.readline

n = int(input())
a,b = map(int,input().split())
m = int(input())

relation = [[] for _ in range(n+1)]
for _ in range(m):
    high, low = map(int,input().split())
    relation[high].append(low)

stack = []
result = 987654321
for i in range(1,n+1):
    stack.append([i,1])
    a_count = b_count = None
    # print(relation)
    while stack:
        high, move = stack.pop()
        # print(high,low,move,'b')
        if high == a:
            a_count = move-1
        elif high == b:
            b_count = move-1
        for low in relation[high]:
            # if low == a:
            #     a_count = move+1
            # elif low == b:
            #     b_count = move+1
            stack.append([low,move+1])
        # print(high,low,move,'a')

    if a_count != None and b_count != None:
        if result>a_count+b_count:
            result = a_count+b_count

if result == 987654321:
    print(-1)
else:
    print(result)