# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

#  0 0 8 arr

white = 0
blue = 0

def solution(x, y, n, arr):

  color = arr[x][y]

  for i in range(x, x + n):
    for j in range(y, y + n):
      if arr[i][j] != color:

        new_n = n // 2
        solution(x,y,new_n,arr)
        solution(x, y + new_n, new_n, arr)
        solution(x + new_n, y, new_n, arr)
        solution(x + new_n, y + new_n, new_n,arr)
        return
  
  if color == 0:
    white += 1
  else:
    blue += 1