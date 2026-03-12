# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819


list_num = [20,1,15,8,4,10]

def solution():
    n = len(list_num)

    for j in range(n):
      for i in range((n-1) - j):
        if list_num[i] > list_num[i + 1]:
          empty_box = list_num[i]
          list_num[i] = list_num[i + 1]
          list_num[i + 1] = empty_box

    k = n // 2
    min_list = list_num[:k]
    min = min_list.pop(1)
    
    min_list.append(min)
    max_list = list_num[k:]

    result = []
    for i in range(k):
      result.append(min_list[i])
      result.append(max_list[(k-1) - i])

    test = result.pop(-2)
    result.append(test)
    print(result)

    sum_num = 0
    
    for j in range(len(result) - 1):
      if result[i] > result[i+1]:
        
        sum_num += result[i] - result[i+1]
    
    print(sum_num)

solution()