# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244


def solution():
  n = 5
  m = 4

  for i in range(1, m + 1):
    print(0, i)

  for i in range(m + 1, n):
    print(i-1, i)
  
solution()