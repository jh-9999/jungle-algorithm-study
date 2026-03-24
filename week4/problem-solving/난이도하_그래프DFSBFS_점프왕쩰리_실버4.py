# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173



from collections import deque


def solution():
  n = int(input())

  board = [list(map(int, input().split())) for _ in range(n)]

  visited = [[False] * n for _ in range(n)]

  x = 0
  y = 0

  queue = deque()
  queue.append((x,y))

  while queue:
    x, y = queue.popleft()

    if x >= n or y >= n: continue
    if visited[x][y]: continue


    move = board[x][y]
    visited[x][y] = True
    if move == -1: break
    queue.append((x+move,y))
    queue.append((x,y+move))
  
  if visited[n-1][n-1]:
    return print("HaruHaru")
  else:
    print("Hing")
    


solution()