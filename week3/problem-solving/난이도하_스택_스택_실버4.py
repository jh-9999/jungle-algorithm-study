# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

import sys

input = sys.stdin.read

def solution():
  data = input().splitlines()
  n = int(data[0])
  commands = data[1:]

  stack = []

  for cmd in commands:
    parts = cmd.split()
    operation = parts[0]

    if operation == "push":
        value = int(parts[1])
        stack.append(value)
        
    elif operation == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
            
    elif operation == "size":
        print(len(stack))
        
    elif operation == "empty":
        print(1 if not stack else 0)
        
    elif operation == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])


solution()