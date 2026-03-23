# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

def solution():
  n = int(input())

  board = [list(map(int, input().split())) for _ in range(n)]

  visited = [[False] * n for _ in range(n)]

  def dfs(x,y):
    if x >= n or y >= n:
      return
    
    if visited[x][y]:
      return
    
    visited[x][y] = True

    if board[x][y] == -1:
      return

    step = board[x][y]

    dfs(x + step,y)
    dfs(x, y + step)
  
  dfs(0,0)
  
  if visited[n-1][n-1]:
    print("HaruHaru")
  else:
    print("Hing")

solution()