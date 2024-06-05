import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def makeTree(currentNode, parent):
    for node in tree[currentNode]:
        if node != parent:
            children[currentNode].append(node)
            makeTree(node, currentNode)

def countSubtreeNodes(currentNode):
    size[currentNode] = 1
    for node in children[currentNode]:
        countSubtreeNodes(node)
        size[currentNode] += size[node]

n, r, q = map(int, input().split())
tree = [[] for _ in range(n + 1)]
children = [[] for _ in range(n + 1)]
size = [0] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

makeTree(r, -1)
countSubtreeNodes(r)

for _ in range(q):
    u = int(input())
    print(size[u])