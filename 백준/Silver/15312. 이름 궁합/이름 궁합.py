import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()

alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

dict = {}
for i in range(len(alp)):
    dict[alp[i]] = str(nums[i])

AB = ""
for i in range(len(A)):
    AB += A[i]
    AB += B[i]

check = ""
for i in range(len(AB)):
    check += dict[AB[i]]

while len(check)>2:
    tmp = ""
    for i in range(1,len(check)):
        tmp += str(((int(check[i-1])+int(check[i]))%10))
    check = tmp

print(check)