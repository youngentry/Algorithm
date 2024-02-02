import sys
input = sys.stdin.readline

for tc in range(3):
    n = int(input())
    
    result = 0
    for _ in range(n):
        result += int(input())
    
    if result > 0: print("+")
    if result == 0: print("0")  
    if result < 0: print("-")