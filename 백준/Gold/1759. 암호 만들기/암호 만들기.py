import sys
from itertools import combinations

l,c = map(int,input().split())
alphabets = list(sorted(input().split()))

candidates = list(combinations(alphabets,l))
# print(candidates)

vowel_set = {'a','e','i','o','u'}
consonant_set = {'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'}

results = []
for candidate in candidates:
    vowel_count = 0
    constant_count = 0
    for alphabet in candidate:
        if alphabet in vowel_set:
            vowel_count += 1
        elif alphabet in consonant_set:
            constant_count += 1
    if vowel_count >= 1 and constant_count >= 2:
        results.append(candidate)

for result in results:
    print("".join(result))
