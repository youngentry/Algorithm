import sys
input = sys.stdin.readline

n = int(input())
a,b = map(int,input().split())
m = int(input())

relation = [[] for _ in range(n+1)]
for _ in range(m):
    high, low = map(int,input().split())
    relation[high].append(low)

# print(relation)

stack = []
result = 987654321
for i in range(1,n+1):
    # print("---------------")
    stack.append([i,1])
    a_count = b_count = None
    while stack:
        high, move = stack.pop()
        # print("high:",high,move)
        # print(high,relation)
        if high ==a:
            a_count = move-1
        elif high ==b:
            b_count = move-1
        for low in relation[high]:
            # print(low,a,b, low==a, low==b)
            if low == a:
                a_count = move+1
            elif low == b:
                b_count = move+1
            stack.append([low,move+1])

        # print(a_count,b_count,"???????????")
    if a_count != None and b_count != None:
        if result>a_count+b_count:
            result = a_count+b_count

if result == 987654321:
    print(-1)
else:
    print(result)