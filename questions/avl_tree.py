"""
Problem: AVL Tree Implementation

Description:
An AVL (Adelson-Velskii and Landis) tree is a self-balancing binary search tree in which the difference between heights of left and right subtrees cannot be more than one for all nodes.

The student should implement the following methods for AVL Tree:
1. insert: Inserts a node into the AVL tree.
2. delete: Removes a node from the AVL tree.
3. balance: Balances the tree whenever necessary after insert or delete operations.
4. rightRotation: Performs right rotation on the tree.

The AVL Tree should be maintained after every insert and delete operation.

Function Signature:
class AVLNode:
    def __init__(self, key, height=1, left=None, right=None):
        self.key = key
        self.height = height
        self.left = left
        self.right = right

class AVLTree:
    ... you may modify the class definition here ...

    def __init__(self, root=None):
        self.root = root

    def delete(self, key) -> None:
        pass

    def balance(self, node: AVLNode) -> AVLNode:
        pass
    
    def rightRotation(self, y: AVLNode) -> AVLNode:
        pass

Examples:
1. AVL tree should rotate right when left child is heavier than right child after an insert operation.
2. AVL tree should balance itself by doing a left rotation when the right child is heavier than the left child after an insert operation.

Tags:
    - AVL Tree
    - Binary Search Tree
    - Trees
    - Rotation
"""

class AVLNode:
    def __init__(self, key, height=1, left=None, right=None):
        self.key = key
        self.height = height
        self.left = left
        self.right = right

class AVLTree:
    def __init__(self, root=None):
        self.root = root

    # This will be a utility method to update height of a node
    def _updateHeight(self, node: AVLNode) -> None:
        if node:
            node.height = 1 + max(self._getHeight(node.left), self._getHeight(node.right))

    def _getHeight(self, node: AVLNode) -> int:
        return node.height if node else 0

    def _getBalance(self, node: AVLNode) -> int:
        return self._getHeight(node.left) - self._getHeight(node.right) if node else 0

    def insert(self, key) -> None:
        self.root = self._insert(self.root, key)
    
    def _insert(self, node: AVLNode, key) -> AVLNode:
        if not node:
            return AVLNode(key)

        # Normal BST insertion
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        # Update height
        self._updateHeight(node)

        # Balance the node
        return self.balance(node)
    
    # TODO: Implement delete method, rightRotation method and balance method

    def rightRotation(self, y: AVLNode) -> AVLNode:
        return AVLNode(0)

    def balance(self, node: AVLNode) -> AVLNode:
        return AVLNode(0)
    
    def delete(self, key) -> None:
        return None