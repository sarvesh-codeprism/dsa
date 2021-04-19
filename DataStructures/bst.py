#!/usr/bin/env python3

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode:
                if not currentNode.left:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if not currentNode.right:
                    currentNode.right = BST(value)
                else:
                    currentNode = currentNode.right
        return self

    def contains(self, value):
        currentNode = self
        while currentNode:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.right:
                currentNode = currentNode.right
            else:
                return currentNode.value == value
        return False
