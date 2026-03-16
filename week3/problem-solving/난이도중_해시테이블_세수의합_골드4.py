# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

import sys

def solution():
  input_data = sys.stdin.read().split()
  if not input_data:
    return
  
  n = int(input_data[0])

  u = list(map(int, input_data[1:]))

  u.sort()

  sums_set = set()

  for i in range(n):
    for j in range(n):
      sums_set.add(u[i] + u[j])
  
  for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
      target = u[i] - u[j]
      if target in sums_set:
        print(u[i])
        return

solution()