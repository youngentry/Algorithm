import sys

input = sys.stdin.readline
word = input().strip()
result = ""
i = 0

while i < len(word):
    if i < len(word)-3 and word[i]+word[i+1]+word[i+2]+word[i+3] == "XXXX":
        result += "AAAA"
        i += 4
    elif i < len(word)-1 and word[i]+word[i+1] == "XX":
        result += "BB"
        i += 2
    else:
        result += word[i]
        i += 1

if "X" in result:
    print(-1)
else:
    print(result)