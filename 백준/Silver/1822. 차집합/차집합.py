import sys
input = sys.stdin.readline

A, B = map(int,input().split())

a_set = set(map(int,input().split()))
b_nums = list(map(int,input().split()))

for del_num in b_nums:
    if del_num in a_set:
        a_set.remove(del_num)

print(len(a_set))
print(" ".join(map(str, sorted(list(a_set)))))