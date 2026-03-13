# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

  
def solution(x, y, n):
  white = 0
  blue = 0
  n = 8
  arr = []
  x = 0
  y = 0

  for i in range(n):
    for j in range(n):
      if arr[i][j] != 1:
        solution(x,y,n // 2)
        solution(x, y + n//2, n // 2)
        solution(x + n//2,y,n // 2)
        solution(x + n//2,y + n//2, n // 2)
      blue += 1
      return
  
