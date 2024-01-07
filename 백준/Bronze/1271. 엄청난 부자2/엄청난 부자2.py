import sys

input = sys.stdin.readline

n, m = map(int,input().split())
# 가진 돈 n, 생명체 수 m

print(n//m)
print(n%m)


