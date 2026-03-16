# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190

from collections import deque

def solution():

  n = 6

  apples = [(3,4), (2,5), (5,3)]

  moves = {3: 'D', 15: 'L', 17: 'D'}

  board = [[0] * (n + 1) for _ in range(n + 1)]

  for r, c in apples:
    board[r][c] = 2
  
  dr = [0, 1, 0, -1]
  dc = [1, 0, -1, 0]
  direction = 0

  curr_r, curr_c = 1,1
  board[curr_r][curr_c] = 1
  snake = deque([curr_r, curr_c])

  time = 0

  while True:
    time += 1

    nr = curr_r + dr[direction]
    nc = curr_r + dc[direction]

    if not (1 <= nr <= n and 1 <= nc <= n) or board[nr][nc] == 1:
      return time
    
    if board[nr][nc] == 2:
      board[nr][nc] = 1
      snake.append((nr,nc))
    else:
      board[nr][nc] = 1
      snake.append((nr, nc))
      tail_r, tail_c = snake.popleft()
      board[tail_r][tail_c] = 0

    curr_r, curr_c = nr, nc

    if time in moves:
      if moves[time] == 'D':
        direction = (direction + 1) % 4
      else:
        direction = (direction - 1) % 4