# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

def solution():
  target = 5
  list_num = [1,3,7,9,8]
  list_num.sort()
  left = 0
  right = len(list_num) - 1
  mid = (left+right)//2

  while left <= right:
    if list_num[mid] == target:
      return print("1")
    if target < list_num[mid]:
      right = mid - 1
      mid = (left + right)//2
    elif target > list_num[mid]:
      left = mid + 1
      mid = (left + right)//2
  
  print("0")


solution()