# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

from collections import deque

n = 3
board =[]

visited = [[False] * n for _ in range(n)]
queue = deque([0,0])
visited[0][0] = True

while queue:
  x, y = queue.popleft()

  if board[x][y] == -1:
    print("HaruHaru")
    break
  
  jump = board[x][y]

  nx = x + jump
  ny = y

  if nx < n and not visited[nx][ny]:
    visited[nx][ny] = True
    queue.append((nx, ny))

  nx = x
  ny = y + jump
  if ny < n and not visited[nx][ny]:
    visited[nx][ny] = True
    queue.append((nx, ny))
else:
  print("Hing")