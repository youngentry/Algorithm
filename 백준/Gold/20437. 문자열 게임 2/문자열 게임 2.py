import sys
input = sys.stdin.readline


# 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이
# 어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이


T = int(input())
for i in range(T):
    alps = [[] for _ in range(26)]
    W = input().strip()
    K = int(input())

    for idx in range(len(W)):
        alps[ord(W[idx])-ord('a')].append(idx)

    min_length = len(W)
    max_length = 0
    is_exist = False
    for alp_idxs in alps:
        if len(alp_idxs) >= K:
            is_exist = True
            for j in range(len(alp_idxs)-K+1):
                min_length = min(min_length,-alp_idxs[j]+alp_idxs[j+K-1]+1)
                max_length = max(max_length,-alp_idxs[j]+alp_idxs[j+K-1]+1)

    if is_exist:
        print(min_length, max_length)
    else:
        print(-1)