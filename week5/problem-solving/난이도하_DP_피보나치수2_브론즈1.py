# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

import sys

def solution():
  input = sys.stdin.readline
    
  n = int(input().strip())
    
  def fibo(num, memo = None):
      if memo is None:
        memo = {}

      if num == 0:
          return 0
      if num == 1:
          return 1

      if num in memo:
        return memo[num]

      memo[num] = fibo(num - 1, memo) + fibo(num - 2, memo)

      return memo[num]

  print(fibo(n))

if __name__ == "__main__":
    solution()