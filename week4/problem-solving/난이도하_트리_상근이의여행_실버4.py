# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

# 모든 나라를 연결하면서 간선 수를 최소로 하는 구조, 신장 트리

import sys

def solution():
    
    t = int(sys.stdin.readline())
    
    
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        
        for _ in range(m):
            sys.stdin.readline()
            
        print(n - 1)

if __name__ == "__main__":
    solution()