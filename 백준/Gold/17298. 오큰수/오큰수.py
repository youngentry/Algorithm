import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int,input().split()))

arr = [0]*1_000_000
st = []

for i in range(N):                             # st의 마지막 수보다 작거나 같으면 스택에 넣기
    if not st:                                 # st가 비어 있으면 게속 넣기
        st.append(i)
        continue
    
    if st and numbers[st[-1]] >= numbers[i]:   # 작거나 같은 수는 st에 넣기
        st.append(i)
        continue
    
    while st and numbers[st[-1]] < numbers[i]: # st의 마지막보다 큰 "오큰수"를 만났다면 
        arr[st.pop()] = numbers[i]             # pop한 인덱스에 오큰수를 저장
    st.append(i)                               # 오큰수 자기 자신을 st에 넣고 계속 반복

while st:
    arr[st.pop()] = -1                         # 오큰수가 없기 때문에 st에 남은 index에 -1을 저장

for i in range(N):
    if arr[i] == 0:
        break

    print(arr[i],end=' ')