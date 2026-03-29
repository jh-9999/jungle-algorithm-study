# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084



#질문 사항 1 왜 초기 값은 1로 해도 나머지 값이 돌아가는지.

import sys

def solution():

  input = sys.stdin.readline

  T = int(input().strip())

  for _ in range(T):
    
    N = int(input().strip())
    
    coins = list(map(int, input().split()))
    
    M = int(input().strip())

    arr = [0] * (M + 2)

    arr[0] = 1

    for coin in coins:
      for i in range(coin, M+1):
        arr[i] = arr[i] + arr[i - coin]
    
    print(arr[M])
    

