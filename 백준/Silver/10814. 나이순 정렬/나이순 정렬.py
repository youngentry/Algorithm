import sys

input = sys.stdin.readline

T = int(input())

words = []
for _ in range(T):
    num, name = input().split()
    num = int(num)
    
    words.append([num,name])

sorted_words = sorted(words,key=lambda x:(x[0]))

for sorted_word in sorted_words:
    print(sorted_word[0], sorted_word[1])