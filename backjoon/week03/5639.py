from sys import stdin as s
from sys import setrecursionlimit
setrecursionlimit(100000)

s = open("input.txt", "rt")
""" 
문제

이진 검색 트리를 전위 순회한 결과가 주어졌을 때, 
이 트리를 후위 순회한 결과를 구하는 프로그램을 작성하시오.

트리를 전위 순회한 결과가 주어진다. 
노드에 들어있는 키의 값은 106보다 작은 양의 정수이다. 
모든 값은 한 줄에 하나씩 주어지며, 
노드의 수는 10,000개 이하이다. 같은 키를 가지는 노드는 없다.

입력으로 주어진 이진 검색 트리를 후위 순회한 결과를 한 줄에 하나씩 출력한다.
"""
# 노드 클래스 구현
class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None

# 이진 탐색 트리 클래스 구현
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, key) -> bool:
        newNode = Node(key)

        if self.root == None:
            self.root = newNode
        else:
            currentNode = self.root

            while True:
                if key < currentNode.key:
                    if currentNode.left is not None:
                        currentNode = currentNode.left
                    else:
                        currentNode.left = newNode
                        break
                else:
                    if currentNode.right is not None:
                        currentNode = currentNode.right
                    else:
                        currentNode.right = newNode
                        break

    # 후위 순외 구현 - recursion limit 제거  
    def postOrder(self, node):
        if not node.left == None:
            self.postOrder(node.left)
        
        if not node.right == None:
            self.postOrder(node.right)

        print(node.key)

if __name__ == "__main__":
    keys = [int(s.rstrip()) for s in s.readlines()]
    bst = BinarySearchTree()

    for key in keys:
        bst.insert(key)

    bst.postOrder(bst.root)