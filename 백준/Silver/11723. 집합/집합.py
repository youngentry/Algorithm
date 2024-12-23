import sys

input = sys.stdin.readline

tup = set()

M = int(input())

for i in range(M):
    line = input().strip()
    if line == 'all' or line == 'empty':
        order = line
    else:
        order, x = line.split(' ')
        x = int(x)

    if order == 'add':
        tup.add(x)

    if order == 'remove':
        if x in tup:
            tup.remove(x)

    if order == 'check':
        if x in tup:
            print('1')
        else:
            print('0')

    if order == 'toggle':
        if x in tup:
            tup.remove(x)
        else:
            tup.add(x)

    if order == 'all':
        tup = set(range(1, 21))

    if order == 'empty':
        tup = set()
