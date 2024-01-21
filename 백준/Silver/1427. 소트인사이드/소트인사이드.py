import sys

input = sys.stdin.readline

word = sorted(list(map(str,input().strip())), reverse=True)


print("".join(word))