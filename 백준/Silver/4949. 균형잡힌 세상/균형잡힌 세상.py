import sys
input = sys.stdin.readline

while True:
    line = input().rstrip()
    if line == ".":
        break

    st = []
    is_good = True
    for word in line:
        # 왼쪽이면 넣음
        if word =="(" or word =="[":
            st.append(word)
            continue
        
        # 오른쪽이면 뺌
            
        if (word == ")" or word == "]") and not st:
            is_good = False
            break
        elif word == ")" and st[-1] == "(":
            st.pop()
        elif word == "]" and st[-1] == "[":
            st.pop()
        elif word == ")" and st[-1] == "[":
            is_good = False
            break
        elif word == "]" and st[-1] == "(":
            is_good = False
            break
    
    if st:
        is_good = False

    if is_good:
        print("yes")
    else:
        print('no')