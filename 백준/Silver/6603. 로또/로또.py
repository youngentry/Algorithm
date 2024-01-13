import sys

input = sys.stdin.readline

flag = True

def comb(lst, n): # n개를 선택
  result = []

  def _comb(start, chosen_lst):
    if len(chosen_lst) == n: # n개가 되면
      result.append(sorted(chosen_lst[:])) # 뽑은 목록 추가
      return # 재귀 종료
    for i in range(start, len(lst)):
      chosen_lst.append(lst[i]) # n번째 요소 추가
      _comb(i+1, chosen_lst)
      chosen_lst.pop() # 상태 복원

  _comb(0,[])
  return result

answer = []

while flag:
  numbers = list((map(int,input().split())))
  sorted_numbers = sorted(numbers[1:])
  pick = 6

  combination = sorted(comb(sorted_numbers,pick))
  if len(numbers) == 1:
    flag = False
  else:
    answer.append(combination)


for i in range(len(answer)):
  for pick in answer[i]:
    print(" ".join(list(map(str,(pick)))))
  if i != len(answer)-1:
    print()
