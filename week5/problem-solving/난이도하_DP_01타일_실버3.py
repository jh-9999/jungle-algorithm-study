# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

import sys

def solution():
  input = sys.stdin.readline

  n = int(input().strip())
  
  arr = [0] * (n + 2)

  arr[0] = 1
  arr[1] = 1

  for i in range(2,n + 1):
    arr[i] = (arr[i - 1] + arr[i - 2]) % 15746

  return print(arr[n])
  
if __name__ == "__main__":
    solution()

