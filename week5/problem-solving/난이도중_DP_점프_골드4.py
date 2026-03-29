# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253

import sys

def solution():
  n, m = map(int, sys.stdin.readline().split())
  traps = set(int(sys.stdin.readline()) for _ in range(m))

  max_jump = 150
  dp = [[float('inf')] * max_jump for _ in range(n + 1)]
  
  if 2 not in traps:
    dp[2][1] = 1

  for i in range(2, n+1):
    for j in range(1, max_jump):
      if dp[i][j] == float('inf'):
        continue

      for v in [j-1, j, j+1]:
        next_stone = i + v

        if v > 0 and v < max_jump and next_stone <= n and next_stone not in traps:
          dp[next_stone][v] = min(dp[next_stone][v],dp[i][j] + 1)
  
  answer = min(dp[n])
  if answer == float('inf'):
    print(-1)
  else:
    print(answer) 
solution()


