N = int(input())
broken_count = int(input())
brokens = []
if broken_count != 0:
    brokens = list(map(int,input().split()))

# +-버튼 눌러서 이동
min_count = 987654321
min_count = min(min_count, abs(N-100))

# 버튼 중복순열
buttons = []
for i in range(10):
    if i not in brokens:
        buttons.append(i)

path = []
def permu(idx, size):
    global min_count

    if path:
        tmp = int("".join(map(str,path)))
        if tmp > N:
            min_count = min(min_count, tmp - N + len(path))
        else:
            min_count = min(min_count, N - tmp + len(path))

    if idx == 6:
        return

    for i in range(size):
        path.append(buttons[i])
        permu(idx+1, size)
        path.pop()



permu(0,len(buttons))

print(min_count)
