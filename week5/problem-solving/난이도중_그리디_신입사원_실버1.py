# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946

import sys

def solution():
  T= int(sys.stdin.readline())

  for _ in range(T):

    N = int(sys.stdin.readline())

    list_ = []

    for _ in range(N):
      p, i = map(int, sys.stdin.readline().split())
      list_.append((p, i))

    list_.sort(key=lambda x: x[0])

    paper, interview = list_[0]

    count = 1

    for i in range(1, len(list_)):
      current_paper, current_interview = list_[i]

      if interview > current_interview:
        count += 1
        interview = current_interview

    print(count)


solution()