"""
[연습 문제 - 트리 순회 복원]

문제 설명:
정점의 값이 모두 서로 다른 이진 트리가 있다. 이 트리의 전위 순회 결과와 중위 순회
결과가 주어졌을 때, 후위 순회 결과를 출력하라.

입력:
- 첫째 줄에 정점의 개수 N이 주어진다. (1 <= N <= 10^5)
- 둘째 줄에 전위 순회 결과 N개가 공백으로 주어진다.
- 셋째 줄에 중위 순회 결과 N개가 공백으로 주어진다.

출력:
- 후위 순회 결과를 공백으로 출력한다.

예제 입력:
5
1 2 4 5 3
4 2 5 1 3

예제 출력:
4 5 2 3 1
"""

import sys


def solve(n, preorder, inorder):
    idx = {value: i for i, value in enumerate(inorder)}

    def sol(pr_l,pr_r,in_l,in_r):

        if pr_l > pr_r:
            return []
        
        root = preorder[pr_l]
        mid = idx[root]

        left_size = mid - in_l

        left = sol(pr_l + 1, pr_l + left_size,in_l,mid-1)
        right = sol(pr_l+left_size+1,pr_r,mid+1,in_r)

        return left + right +[root]


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    preorder = list(map(int, data[1 : 1 + n]))
    inorder = list(map(int, data[1 + n : 1 + 2 * n]))
    result = solve(n, preorder, inorder)
    if result:
        sys.stdout.write(" ".join(map(str, result)))


if __name__ == "__main__":
    main()

