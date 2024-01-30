import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())

def get_mod(b):
    if b == 1:
        return a%c
    else:
        if b%2==0:
            return get_mod(b//2)**2 %c
        else:
            return get_mod(b//2)**2 *a %c
result = get_mod(b)
print(result)