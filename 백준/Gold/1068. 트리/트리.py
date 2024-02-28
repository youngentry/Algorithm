# 잎 개수 찾기
def trav(node):
    global leaf

    for num in node:
        if not tree[num]:
            leaf += 1
        else:
            trav(tree[num])

N = int(input())
numbers = list(map(int,input().split()))
root = None
# 트리 그리기
tree = [[] for _ in range(51)]
for i in range(N):
    if numbers[i] == -1:
        root = i
    tree[numbers[i]].append(i)

leaf = 0
쳐내 = int(input())
for leafs in tree:
    if 쳐내 in leafs:
        leafs.remove(쳐내)
    if 쳐내 == root:
        tree[쳐내] = []

# 쳐낸 대상이 브랜치나 잎이면
if tree[root]:
    trav(tree[root]) # 잎 개수 찾기
    print(leaf)
# 쳐낸 대상이 루트면
elif 쳐내 == root:
    print(0)
# 루트가 리프라면
else:
    print(1)

