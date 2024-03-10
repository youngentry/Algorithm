import sys
input = sys.stdin.readline

S = list(input().strip())
T = list(input().strip())

slength = len(S)

while len(T) > slength:
    if T[-1] == "A":
        T.pop()
    else:
        T.pop()
        T.reverse()

if T == S:
    print(1)
else:
    print(0)