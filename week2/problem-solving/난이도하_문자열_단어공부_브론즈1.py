# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.

import sys

def solution():
  
  target = sys.stdin.readline().strip()

  upper_text = target.upper()
  dir = {}

  for i in range(len(target)):
    if upper_text[i] not in dir:
      dir[upper_text[i]] = 1
    else: dir[upper_text[i]] += 1
  
  max = 0
  result = ""
  for i in range(len(target)):
    if max < dir[upper_text[i]]:
      max = dir[upper_text[i]]
      result = upper_text[i]
  
  for i in range(len(target)):
    if result != upper_text[i] and max ==dir[upper_text[i]]:
      return print("?")

  print(result)
  

solution()