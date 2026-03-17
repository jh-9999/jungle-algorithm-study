# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629

import sys

def solution(a,b,c):
  
  if b == 1:
    return a % c
  
  temp = solution(a, b // 2, c)

  if b % 2 == 0:
    return (temp * temp) % c
  else:
    return (temp * temp * a) % c
  

a, b, c = map(int, sys.stdin.readline().split())

print(solution(a,b,c))