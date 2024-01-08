import sys

input = sys.stdin.readline

exp = input()
flag = False

exp_list = exp.split("-")
# print(exp_list)

for i in range(len(exp_list)):
  exp_list[i] = list(map(int,exp_list[i].split("+")))

# print(exp_list)
result = 0
for i in range(len(exp_list)):
  for number in exp_list[i]:
    if i == 0:
      result += number
    else:
      result -= number

print(result)




# for i in range(len(exp)):
#   if exp[i] == "-" and not flag:
#     exp = exp[0:i] + "-(" + exp[i + 1:]
#     i += 1
#     flag = not flag
#   elif exp[i] == "-" and flag:
#     exp = exp[0:i] + ")" + exp[i + 1:]
#     flag = not flag

# last = ""
# if flag:
#   last = ")"
  
# print(eval(exp + last))

# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식 만들고
# 괄호를 모두 지웠다
# 괄호를 적절히 쳐서 이 식의 값을 최소로

