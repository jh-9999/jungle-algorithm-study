# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

# 모든 나라를 연결하면서 간선 수를 최소로 하는 구조, 신장 트리

T = 5

for _ in range(T):
  N, M = map(int, input().split())

  for _ in range(M):
    input()
  
  print(N - 1)