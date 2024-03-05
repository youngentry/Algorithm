import sys
input = sys.stdin.readline

def is_prime(num):
    if num == 1:
        return False
    
    for i in range(2,int(num**(1/2))+1):
        if num%i == 0:
            return False
    
    return True


def check(num):
    left = right = num//2

    while True:
        if not (is_prime(left) and is_prime(right)):
            left-=1
            right+=1
            continue

        return print(left, right)


N = int(input().strip())
for _ in range(N):
    num = int(input())
    check(num)