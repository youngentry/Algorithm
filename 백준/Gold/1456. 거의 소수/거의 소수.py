import sys
input = sys.stdin.readline
import math

A,B = map(int,input().split())

# 1. 10000000 까지 에라토스테네스의 채로 거름
# 2. 소수에 대해 10000000보다 작을 때까지 제곱한 수를 더함
primes = [0]*(int(B**(0.5))+1)
primes[1] = 0
primes[2] = 2
for i in range(3,(len(primes)),2):
    primes[i] = i
for i in range(3, len(primes),2):
    if primes[i] == 0:
        continue
    for j in range(i*2, (len(primes)),i):
        primes[j] = 0

ans = 0
for i in primes:
    if i:
        check = i**2
        while check <= B:
            if A <= check:
                ans += 1
            check *= i

print(ans)