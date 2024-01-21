import sys
input = sys.stdin.readline

N=int(input()) # 총 단어의 개수
count=N # 그룹 단어가 몇 개인지 알기 위해서 그룹단어가 아닌 단어를 만나면 1씩 뺄 예정
for test_case in range(N):
    word = input()
    for i in range(len(word)-1): # 단어 길이만큼 돌리면 바로 밑 if문에서 range값을 초과한다. 
																	# 어차피 마지막 글자는 비교할 필요 없으니 단어길이-1만큼 돌리기.
        if word[i]==word[i+1]: # 첫 글자부터 바로 다음 글자와 비교했을 때 같으면 그냥 넘어감.
            pass               # continue 쓰면 i값이 증가해서 다음 글자와 비교하게 되므로 pass
        elif word[i] in word[i+1:]: # 다음 글자와 다르다면, 본인 다음 글자들 중에 같은 것이 있는지 체크. 
            count-=1 #있다면 그룹단어가 아니니까 -1
            break # 그룹단어가 아니라는 증거를 하나라도 얻는 순간 끝내야 함. 아니면 증거의 개수만큼 빠진다.
print(count) 