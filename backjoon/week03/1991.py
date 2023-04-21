from sys import stdin as s

s = open("input.txt", "rt")
""" 
문제

이진 트리를 입력받아 
전위 순회(preorder traversal), 
중위 순회(inorder traversal), 
후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

예를 들어 위와 같은 이진 트리가 입력되면,

전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
가 된다.

첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 
둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 
오른쪽 자식 노드가 주어진다. 
노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 
항상 A가 루트 노드가 된다. 
자식 노드가 없는 경우에는 .으로 표현한다.

첫째 줄에 전위 순회,
둘째 줄에 중위 순회, 
셋째 줄에 후위 순회한 결과를 출력한다. 
각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.
"""

# 노드 클래스 구현
class Node:
    def __init__(self, value, left, right) -> None:
        self.value = value
        self.left = left
        self.right = right

# 전위 순회 함수 구현
def preOrder(node):
    """ node : 순회 할 노드 """
    # 1. 부모 노드 출력
    print(node.value, end="")
    # 2. 왼쪽 자식이 존재한다면 순회
    if node.left != ".":
        preOrder(trees[node.left])
    # 3. 오른쪽 자식이 존재한다면 순회
    if node.right != ".":
        preOrder(trees[node.right])

# 중위 순회 함수 구현
def inOrder(node):
    """ node: 순회 할 노드 """
    # 1. 왼쪽 자식 존재한다면 순회
    if node.left != ".":
        inOrder(trees[node.left])
    
    # 2. 부모 노드 출력
    print(node.value, end= "")

    # 3. 오른쪽 자식 존재한다면 순회
    if node.right != ".":
        inOrder(trees[node.right])

# 후위 순회 구현
def postOrder(node):
    """ node: 순회 할 노드 """
    # 1. 왼쪽 자식이 존재한다면 순회
    if node.left != ".":
        postOrder(trees[node.left])
    # 2. 오른쪽 자식이 존재한다면 순회
    if node.right != ".":
        postOrder(trees[node.right])
    # 3. 부모 노드 출력
    print(node.value, end="")


if __name__ == "__main__":
    n = int(s.readline().rstrip())
    vertexs = [list(s.readline().rstrip().split()) for _ in range(n)]
    trees = {}

    for i in range(n):
        root, left, right = vertexs[i]
        trees[root] = Node(root, left, right)


    preOrder(trees["A"])
    print()
    inOrder(trees["A"])
    print()
    postOrder(trees["A"])