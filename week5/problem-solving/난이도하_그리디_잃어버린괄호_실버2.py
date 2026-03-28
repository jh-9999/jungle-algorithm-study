# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

import sys

def solution():
    k = sys.stdin.readline().strip()

    new_list = k.split('-')

    total = 0

    if '+' in new_list[0]:
      plus_list = new_list[0].split('+')
        
      for item in plus_list:
        total += int(item)
    else:
      total += int(new_list[0])


    for i in range(1, len(new_list)):
      if '+' in new_list[i]:
        plus_list = new_list[i].split('+')
        
        for item in plus_list:
          total -= int(item)
      else:
        total -= int(new_list[i])
    
    print(total)

solution()
    
      
