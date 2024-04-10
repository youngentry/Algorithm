import sys
input = sys.stdin.readline

N = int(input())
dict = {}

for i in range(N):
    name, is_visit = input().strip().split()
    if is_visit == "enter":
        dict[name] = 1
    else:
        dict[name] = 0

lst = []
for name, is_true in dict.items():
    if is_true:
        lst.append(name)
lst.sort(reverse=True)
print(*lst,sep='\n')