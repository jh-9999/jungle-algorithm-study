# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

def solution():
    left_stack = ["a", "b", "c", "d"]
    right_stack = []

    commands = [["L"], ["B"], ["P", "x"]] 

    for cmd in commands:
        if cmd[0] == "L":
            if left_stack:
                right_stack.append(left_stack.pop())
        elif cmd[0] == "D": 
            if right_stack:
                left_stack.append(right_stack.pop())
        elif cmd[0] == "B":
            if left_stack:
                left_stack.pop()
        elif cmd[0] == "P":
            left_stack.append(cmd[1])
  
    return left_stack + list(reversed(right_stack))

print(solution())