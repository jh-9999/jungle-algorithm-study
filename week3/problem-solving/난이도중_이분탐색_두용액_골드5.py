# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470


import sys

def solution():

  n = int(sys.stdin.readline())

  list_num = list(map(int, sys.stdin.readline().split()))

  list_num.sort()

  result = [0,0]

  left = 0
  right = n - 1

  min_num = float('inf')

  while left < right:
    current_sum = list_num[left] + list_num[right]
    
    if abs(current_sum) < min_num:
      min_num = abs(current_sum)
      result = [list_num[left],list_num[right]]
    
    if current_sum < 0 :
      left += 1
    elif current_sum > 0:
      right -= 1
    else:
      break

  print(result[0], result[1])

solution()