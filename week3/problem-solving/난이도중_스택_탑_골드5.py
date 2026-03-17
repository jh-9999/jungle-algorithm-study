# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493

import sys

def solution():
  input_data = sys.stdin.read().split()
  if not input_data:
    return


  n =  int(input_data[0])
  list_num = list(map(int, input_data[1:]))
  result = []
  stack = []

  for i in range(n):
    current_top = list_num[i]
    current_num = i + 1

    while stack and stack[-1][0] < current_top:
      stack.pop()
    
    if not stack:
      result.append(0)
    else:
      result.append(stack[-1][1])
    
    stack.append((current_top, current_num))

  print(*(result))

solution()