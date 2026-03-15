# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295


def solution():
  dir = [2, 3, 5, 10, 18]
  dir.sort()

  n = len(dir)

  i = 0
  while True:
    sum_num = dir[i]
