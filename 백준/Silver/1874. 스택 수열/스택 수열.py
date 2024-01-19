import sys
input = sys.stdin.readline

n = int(input())
stack = []

counter = 1

result = []

for _ in range(1,n+1):
    # print(stack,'000')

    num = int(input())

    # 일치하는 값을 찾을 때까지 추가
    while not stack or stack[-1] != num and counter<=n:
        stack.append(counter)
        counter += 1
        result.append("+")
        # print(stack,'111')

    if len(stack) and num < stack[-1]:
        print("NO")
        break
    # print(num, stack)
    
    if len(stack) and stack[-1] == num:
        stack.pop()
        result.append("-")
        # print(stack,"222")
else:
    # print(result, stack)
    if result.count("+") == n:
        [print(oper) for oper in result]