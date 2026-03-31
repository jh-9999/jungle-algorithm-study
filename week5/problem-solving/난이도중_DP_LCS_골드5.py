# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251




def solution():
  a_string = input()
  b_string = input()

  n = len(a_string)
  m = len(b_string)

  arr = [[0] * (m+1) for _ in range(n+1)]

  for i in range(1, n+1):
    for j in range(1, m+1):
      first = a_string[i - 1]
      second = b_string[j - 1]

      if first == second:
        arr[i][j] = arr[i-1][j-1] + 1
      else:
        arr[i][j] = max(arr[i][j-1], arr[i-1][j])

  print(arr[n][m])

solution()


  