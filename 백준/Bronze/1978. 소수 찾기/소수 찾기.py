n = int(input())

def isPrime(number):
  number = int(number)
  if number < 2:
      return False
  if number == 2:
      return True
  if number % 2 == 0:
    return False

  for i in range(3, int(number**0.5)+1, 2):
        if number%i == 0:
            return False

  return True

prime_count = 0

numbers = list(map(int,input().split()))

for number in numbers:
  if isPrime(number):
      prime_count += 1

print(prime_count)