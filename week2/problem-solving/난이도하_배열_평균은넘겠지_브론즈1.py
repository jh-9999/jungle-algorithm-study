# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344
import sys

C = int(sys.stdin.readline())

def solution():

    data = list(map(int, sys.stdin.readline().split()))

    scores = data[1:]

    sum_num = 0
    n = len(scores)
    for score in scores:
      sum_num += score
    
    avarage = sum_num / n

    count = 0

    for score in scores:
      if score >  avarage:
        count += 1
    
    print(f"{(count / n) * 100 : .3f}%")

for _ in range(C):
  solution()
