""" 이진탐색트리 구현 """

# 노드 클래스
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value) -> bool:
        newNode = Node(value)

        if self.root == None:
            self.root = newNode
        else:
            currentNode = self.root

            while True:
                if value < currentNode.value:
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

    def preOrder(self, node):
        print(node.value)
        if not node.left == None:
            self.preOrder(node.left)
        if not node.right == None:
            self.preOrder(node.right)

    def inOrder(self, node):
        if not node.left == None:
            self.inOrder(node.left)
        print(node.value)
        if not node.right == None:
            self.inOrder(node.right)

    def postOrder(self, node):
        if not node.left == None:
            self.postOrder(node.left)
        if not node.right == None:
            self.postOrder(node.right)
        print(node.value)

