# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606



from inspect import stack


def solution():
  n = int(input())
  m = int(input())

  graph = [[] for _ in range(n + 1)]

  for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
  
  visited = [False] * (n + 1)

  start = 1

  visited[start] = True

  stack = []

  stack.append(start)

  result = []

  while stack:
    current = stack.pop()
    
    for nex in graph[current]:
      if not visited[nex]:
        visited[nex] = True
        result.append(nex)
        stack.append(nex)
  
  print(len(result))

solution()

# from collections import deque

# def solution():
#   n = int(input())
#   m = int(input())

#   graph = [[] for _ in range(n + 1)]

#   for _ in range(m):
#     start, end = map(int, input().split())
#     graph[start].append(end)
#     graph[end].append(start)
  
#   visited = [False] * (n + 1)

#   start = 1

#   queue = deque()

#   visited[start] = True
#   queue.append(start)

#   result = []

#   while queue:
#     current = queue.popleft()

#     for nex in graph[current]:
#       if not visited[nex]:
#         visited[nex] = True
#         result.append(nex)
#         queue.append(nex)
  
#   print(len(result))

# solution()

# def solution():
#   n = int(input())
#   m = int(input())

#   graph = [[] for _ in range(n + 1)]

#   for _ in range(m):
#     start, end = map(int, input().split())
#     graph[start].append(end)
#     graph[end].append(start)

#   visited = [False] * (n + 1)

#   start = 1

#   visited[start] = True

#   result = []
#   def dfs(graph, start, visited):
#     for nex in graph[start]:
#       if not visited[nex]:
#         visited[nex] = True
#         result.append(nex)
#         dfs(graph, nex, visited)

#   dfs(graph,start, visited)
#   print(len(result))
  
# solution()