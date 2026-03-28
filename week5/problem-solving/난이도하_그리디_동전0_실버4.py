# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

import sys

def solution():
  n, k = map(int, input().split())

  numbers =  [int(input()) for _ in range(n)]

  numbers.sort(reverse=True)

  result = 0

  for coin in numbers:
    if coin > k: pass
    
    count = k // coin

    if count != 0:
      k %= coin
      result += count
    
    if k == 0:
      break
  
  print(result)

solution()