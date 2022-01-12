'''
스택을 이용한 풀이
열려있는 괄호의 수를 기억하고 있다가
자르는 선이 나올때, 열려있는 괄호의 수-1만큼 덧셈.
괄호를 닫을때 1 덧셈.
'''

def solution(s):
  stack = []
  open_num = 0
  ans = 0
  
  for c in s:
    if c == '(':
      open_num = open_num+1
      stack.append(c)
    elif c == ')' and stack[-1] == '(': # 자르는 선
      ans = ans+open_num-1
      stack.append(c)
      open_num = open_num-1
      #print("split")
    else:
      ans = ans+1
      open_num = open_num-1
      #print("split")

    #print(stack, open_num, ans)
      
  return ans

if __name__ == "__main__":
  s = input()
  ret = solution(s)
  print(ret)