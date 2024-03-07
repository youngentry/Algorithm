import sys
input = sys.stdin.readline

brackets = input().strip()

st = []
is_bad = False
ans = 0
tmp = 1
for i in range(len(brackets)):
    # 넣어라
    if brackets[i] == "(":
        st.append("(")
        tmp *= 2
    elif brackets[i] == "[":
        st.append("[")
        tmp *= 3

    # 정지해라
    elif not st and brackets[i] =="]":
        is_bad = True
    elif not st and brackets[i] ==")":
        is_bad = True
    elif st[-1] =="(" and brackets[i] =="]":
        is_bad = True
    elif st[-1] =="[" and brackets[i] ==")":
        is_bad = True

    # 빼라, 근데 뭔가 할 일이 있어
    elif st[-1] =="(" and brackets[i] ==")":
        if brackets[i-1] == "(": # 쌍이 맞으면 값 더하기
            ans += tmp
        st.pop()
        tmp //= 2 # 괄호가 벗겨졌으니 다시 나누기
    elif st[-1] =="[" and brackets[i] =="]":
        if brackets[i-1] == "[":
            ans += tmp
        st.pop()
        tmp //= 3

if st: is_bad = True

if is_bad: print(0)
else:      print(ans)