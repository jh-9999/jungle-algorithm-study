# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

list = [1,3,5,7]

def solution():
    count = 0
    for i in list:
      if i == 2:
        count += 1
        continue

      if i % 2 == 0:
        continue

      j = 2
      while i >= j:
        if i % j == 0 and i == j:
          count += 1
          break
        if i % j == 0:
          break
        j += 1
    
    print(count)

solution()