# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933
import sys

def solution():
  n = int(sys.stdin.readline())

  words = set()

  for _ in range(n):
    words.add(sys.stdin.readline().strip())


  def reverse_with_stack(text):
    stack = list(text)
    reversed_list = []
    while stack:
        reversed_list.append(stack.pop())
    return "".join(reversed_list)

  for s in words:
    reversed_text = reverse_with_stack(s)
        
    # 뒤집은 단어가 목록에 있다면 비밀번호!
    if reversed_text in words:
        length = len(s)
        center_char = s[length // 2]
        
        # 길이와 중앙 문자 출력
        print(length, center_char)
        return  # 하나만 찾으면 되므로 즉시 종료
    
solution()