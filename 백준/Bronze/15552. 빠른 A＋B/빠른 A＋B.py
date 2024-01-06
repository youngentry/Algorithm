import sys
input = sys.stdin.readline

T = int(input())

for T_C in range(1,T+1):
    A, B = map(int, input().split())
    print(A+B)