# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

import sys
from collections import deque

def solution():
  input_data = sys.stdin.read().split()

  n = int(input_data[0])

  queue = deque()
  for i in range(1, n + 1):
    queue.append(i)
  
  i = 1
  while len(queue) != 1:
    if i % 2 == 1:
      queue.popleft()
    elif i% 2 == 0:
      num = queue.popleft()
      queue.append(num)
    i += 1
  print(queue[0])

solution()