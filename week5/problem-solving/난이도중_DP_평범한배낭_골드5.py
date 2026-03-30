# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

import sys
from collections import deque

def solution():
  n,k = map(int, sys.stdin.readline().split())

  item_list = []

  for i in range(n):
    k_, v_ = map(int, sys.stdin.readline().split())
    item_list.append((k_, v_))

  item_list.sort(key=lambda x: x[0])

  value_arr = [[0] * (k + 1) for _ in range(n + 1)]

  for i in range(1, n+1):
    weight, value = item_list[i-1]
    for j in range(1, k+1):
      if weight > j:
        value_arr[i][j] = value_arr[i-1][j]
      else:
        value_arr[i][j] = max(value_arr[i-1][j], value_arr[i-1][j - weight] + value)

  print(value_arr[n][k])

solution()