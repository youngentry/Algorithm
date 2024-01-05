T = int(input())

for T_C in range(T):
    brackets = list(input())
    stack = []
    for bracket in brackets:
        if len(stack) and stack[-1] == "(" and bracket ==")":
            stack.pop()
        else:
            stack.append(bracket)
    
    if not len(stack):
        print("YES")
    else:
        print("NO")