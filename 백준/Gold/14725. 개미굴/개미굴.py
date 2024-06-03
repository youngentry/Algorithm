import sys
input = sys.stdin.readline

n = int(input())
lst = [list(input().split()) for _ in range(n)]
lst.sort(reverse=True)

dct = {}

def trie(words):
    cur = dct
    for word in words:
        if word not in cur:
            cur[word] = {}
        cur = cur[word]


for i in range(n):
    trie(lst[i][1:])

def dfs(node,depth):
    for key in sorted(node):
        print(depth*'--' + key)
        dfs(node[key],depth+1)

dfs(dct,0)