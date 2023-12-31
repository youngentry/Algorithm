
# n일이 주어진다
# 연속적인 k일 동안의 온도의 합이 가장 큰 값

n,k = map(int,input().split())
temps = list(map(int,input().split()))


max_temp = sum(temps[:k])
temp_sum = sum(temps[:k])

for i in range(0, n-k):
    temp_sum = temp_sum - temps[i]
    temp_sum = temp_sum + temps[i+k]
    max_temp = max(max_temp,temp_sum)

print(max_temp)