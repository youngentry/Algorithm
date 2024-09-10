import sys
input = sys.stdin.readline

N = int(input())

arr = []

for i in range(N):
    name, n1,n2,n3 = input().split()
    if len(n1) < 2:
        n1 = '0' + n1
    if len(n2) < 2:
        n2 = '0' + n2

    arr.append((name,''.join(reversed([n1,n2,n3]))))

arr.sort(key=lambda x:x[1])

print(arr[-1][0])
print(arr[0][0])
