# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084


import sys



def solution():

  input = sys.stdin.readline

  T = int(input().strip())

  for _ in range(T):
    
    N = int(input().strip())
    
    coins = list(map(int, input().split()))
    
    M = int(input().strip())

    result = 0

    arr = [0] * 10000

    for coin in coins:
      
